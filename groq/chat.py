import streamlit as st
from groq import Groq

favicon = "logo_chat.jpg"

st.set_page_config(page_title="Annelise ChatBot!", page_icon=favicon)

client = Groq(
    api_key="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",
)

st.title("Bem vindo á Annelise ChatBot")

banner_image = "img/banner_avatar.png"

# Adiciona o banner ao aplicativo
st.image(banner_image, use_column_width=True)

# Adiciona uma descrição dos campos de entrada do usuário
st.subheader("Faça sua pergunta:")

# Adiciona um estilo ao campo de entrada do usuário
user_input = st.text_input("", placeholder="Digite sua pergunta aqui...")
context = "Você é uma assistente virtual chamada Annelise, responda as perguntas de forma clara e objetiva na lingua portuguesa."

if user_input:
    chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": context + user_input,
                }
            ],
            model="mixtral-8x7b-32768",
        )

    # Adiciona uma margem à resposta do chatbot
    st.markdown("***Resposta do chatbot:***")
    st.write(chat_completion.choices[0].message.content)
    st.write("**Este chatbot foi criado com o modelo ", chat_completion.model, " usando a API da Groq.**")
    st.write("**O tempo para resposta foi de ", chat_completion.usage.completion_time, " segundos.**")