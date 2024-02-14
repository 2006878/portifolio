import streamlit as st
from PIL import Image
from st_pages import Page, show_pages

# Carreguando o ícone da aba
favicon = "img/dados.png"

# Configurações da página Streamlit
st.set_page_config(page_title="Tairone Amaral", page_icon=favicon)

# Menu lateral
# show_pages(
#     [
#         Page("exemplo1.py", "Exemplo 1", icon="📈"),
#         Page("exemplo2.py", "Exemplo 2", icon="📈")
#     ]
# )

# Define o banner
banner_image = "img/banner.jpeg"

# Adiciona o banner ao aplicativo
st.image(banner_image, use_column_width=True)

# Informações pessoais
st.title("Tairone Leandro do Amaral")
st.write("Graduado em Ciência de Dados pela Universidade Virtual do Estado de São Paulo – UNIVESP.")

# Habilidades
st.subheader("Habilidades")
st.write("Desenvolvimento de software")
st.write("Gerenciamento de Equipe")
st.write("Ciência de Dados")
st.write("Inovação em Negócios")

# Experiências
st.subheader("Experiências")
st.write("Serralheria Amaral (2002 - 2021): Gerente responsável por equipe de produção, processos administrativos financeiros e inovação nos setores da empresa.")
st.write("CM Tecnologia (2021 - 2022): Estagiário, promovido a Analista de Desenvolvimento I, Analista de Desenvolvimento II e Coordenador do time de suporte técnico promovendo o aumento do engajamento da equipe em mais de 100%, aumentando a base de clientes mesmo enfrentando um corte de pessoal mantendo o produto operante e NPS alto.")
st.write("GetinOxy (2022 - 2023): Líder técnico do time back-end e infraestrutura no desenvolvimento de API RestFul. Entrega de API altamente escalável para consumo de aplicações da área de saúde.")
st.write("Serralheria Amaral (Setembro de 2022 - Atual): Diretor Geral, com resultado de aumento de 55% no faturamento anual.")
st.write("Zayon Data Mine (Junho de 2023 - Atual): Cientista de Dados, liderando projetos de pesquisa e desenvolvimento de modelos de Inteligência Artificial. Construção de plataforma integrando ferramentas e análises para otimização de decisões.")
st.write("TaaS (2023 - Atual): 'Talent as a Service', fornecendo suporte estratégico e consultivo a Startups.")

# Hobbies e Objetivos
st.subheader("Hobbies e Objetivos")
st.write("Hobbies: Leitura, prática de Jiu-Jitsu (instrutor) e viagens com a família.")
st.write("Objetivos: Impactar cada vez mais pessoas, colaborando na construção e manutenção de produtos e projetos que impactem positivamente a vida delas.")

# Contatos
st.subheader("Contatos")
st.write("Telefone: 35 992579211")
st.write("LinkedIn: [Perfil do LinkedIn de Tairone Amaral](https://www.linkedin.com/in/tairone-amaral/)")

qr_linkedin = "img/QRLinkedin.png"
st.image(qr_linkedin, use_column_width=False, width=150)