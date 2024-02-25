import streamlit as st
import numpy as np
import pandas as pd
import joblib
from predict.dictionary import dictionary_diseases, dictionary_symptoms
import os

# Load data and model
full_path = os.getcwd()
df_severity = pd.read_csv(full_path + "/predict/csv/Symptom-severity.csv")
modelo = joblib.load(full_path + "/predict/model_predict_disease.pkl")

# Define symptom-to-weight function
def sintomas_para_pesos(sintomas_de_entrada):
    pesos_de_sintomas = df_severity.set_index("Symptom")["weight"].to_dict()
    pesos = [pesos_de_sintomas[sintoma] for sintoma in sintomas_de_entrada]
    return pesos

# Streamlit app
st.title("Apoio ao profissional de saúde no pré-diagnóstico de doenças.")
st.markdown("#### Selecione os sintomas:")

# Criando um novo dicionário com sintomas capitalizados
capitalized_symptoms = {sintoma.title(): sintoma for sintoma in dictionary_symptoms.keys()}

# MultiSelect widget for symptoms
selected_sintomas = st.multiselect("Sintomas:", list(capitalized_symptoms.keys()))

# Convertendo os sintomas selecionados de volta para minúsculas para a busca
selected_sintomas = [capitalized_symptoms[sintoma] for sintoma in selected_sintomas]

# Handle empty input
if not selected_sintomas:
    st.error("Por favor, selecione pelo menos um sintoma.")
    st.stop()

# Predict disease
sintomas_portugues = list(selected_sintomas)
sintomas_de_entrada = list(
    map(lambda sintoma: dictionary_symptoms.get(sintoma, sintoma), sintomas_portugues)
)
df_severity["Symptom"] = df_severity["Symptom"].str.replace("_", " ")
pesos_de_entrada = sintomas_para_pesos(sintomas_de_entrada)

while len(pesos_de_entrada) < 17:
    pesos_de_entrada.append(0)

doenca_prevista = modelo.predict([pesos_de_entrada])[0]
doenca_portugues = dictionary_diseases.get(doenca_prevista, doenca_prevista)

# Load descriptions and precautions
df_description = pd.read_csv(full_path + "/predict/csv/symptom_Description_pt.csv")
df_precaution = pd.read_csv(full_path + "/predict/csv/symptom_precaution_pt.csv")

description = df_description[df_description["Disease"] == doenca_prevista][
    "Description"
].values[0]
precautions = [
    precaution
    for precaution in df_precaution[df_precaution["Disease"] == doenca_prevista][
        "Precaution_1"
    ].values
    if precaution != "" and precaution is not np.nan
]
precautions += [
    precaution
    for precaution in df_precaution[df_precaution["Disease"] == doenca_prevista][
        "Precaution_2"
    ].values
    if precaution != "" and precaution is not np.nan
]
precautions += [
    precaution
    for precaution in df_precaution[df_precaution["Disease"] == doenca_prevista][
        "Precaution_3"
    ].values
    if precaution != "" and precaution is not np.nan
]
precautions += [
    precaution
    for precaution in df_precaution[df_precaution["Disease"] == doenca_prevista][
        "Precaution_4"
    ].values
    if precaution != "" and precaution is not np.nan
]

precautions_string = ", ".join(precautions)
if precautions_string:
    precautions_string = precautions_string.capitalize()

# Display results
st.markdown("#### De acordo com os sintomas informados acima, a hipótese diagnóstica é:")
st.write(doenca_portugues)

st.markdown("#### Descrição:")
st.write(description)

if precautions_string:
    st.markdown("#### Precauções Recomendadas:")
    st.write(precautions_string)

st.warning(
    "Esta versão do aplicativo foi treinado com algorítmos de aprendizado de máquina em um conjunto pequeno de dados e fornece apenas uma previsão preliminar e não substitui o diagnóstico e tratamento médico profissional."
)
