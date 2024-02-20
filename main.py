import streamlit as st
# from PIL import Image
from st_pages import Page, show_pages
import base64
# from email.mime.text import MIMEText
# import smtplib
import webbrowser
from urllib.parse import quote

# Carreguando o ícone da aba
favicon = "img/dados.png"

# Configurações da página Streamlit
st.set_page_config(page_title="Tairone Amaral", page_icon=favicon)

# Menu lateral
show_pages(
    [
        Page("main.py", "Home", icon="📊"),
        Page("exemplo1.py", "Nuvem de Palavras", icon="📈")
    ]
)

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
st.markdown("---")

# Experiências
st.subheader("Experiências")
st.write("Serralheria Amaral (2002 - 2021): Gerente responsável por equipe de produção, processos administrativos financeiros e inovação nos setores da empresa.")
st.write("CM Tecnologia (2021 - 2022): Estagiário, promovido a Analista de Desenvolvimento I, Analista de Desenvolvimento II e Coordenador do time de suporte técnico promovendo o aumento do engajamento da equipe em mais de 100%, aumentando a base de clientes mesmo enfrentando um corte de pessoal mantendo o produto operante e NPS alto.")
st.write("GetinOxy (2022 - 2023): Líder técnico do time back-end e infraestrutura no desenvolvimento de API RestFul. Entrega de API altamente escalável para consumo de aplicações da área de saúde.")
st.write("Serralheria Amaral (Setembro de 2022 - Atual): Diretor Geral, com resultado de aumento de 55% no faturamento anual.")
st.write("Zayon Data Mine (Junho de 2023 - Atual): Cientista de Dados, liderando projetos de pesquisa e desenvolvimento de modelos de Inteligência Artificial. Construção de plataforma integrando ferramentas e análises para otimização de decisões.")
st.write("TaaS (2023 - Atual): 'Talent as a Service', fornecendo suporte estratégico e consultivo a Startups.")
st.markdown("---")

# Hobbies e Objetivos
st.subheader("Hobbies e Objetivos")
st.write("Hobbies: Leitura, prática de Jiu-Jitsu (instrutor) e viagens com a família.")
st.write("Objetivos: Impactar cada vez mais pessoas, colaborando na construção e manutenção de produtos e projetos que impactem positivamente a vida delas.")
st.markdown("---")

# Contatos
st.subheader("Contato")

# with st.form(key="contato"):
#     nome = st.text_input("Nome")
#     email = st.text_input("Email")
#     mensagem = st.text_area("Mensagem")
#     submit = st.form_submit_button("Enviar")

# if submit:

#     # Crie a mensagem
#     mensagem = f"""
#     Nome: {nome}\n
#     Email: {email}\n
#     Mensagem: {mensagem}
#     """
#     mensagem = quote(mensagem)
#     whatsapp_url = f"https://api.whatsapp.com/send?phone=5535992579211&text={mensagem}"
#     webbrowser.open(whatsapp_url)

#     # Exiba uma mensagem de sucesso
#     st.success("Mensagem enviada com sucesso!")

link_url = "https://www.linkedin.com/in/tairone-amaral/"
link_wpp = "https://api.whatsapp.com/send?phone=5535992579211"
qr_linkedin = "img/QRLinkedin.png"
qr_whatsapp = "img/logo_wpp.png"

# Adiciona os QRCode dos contatos
def get_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

image_linkedin = get_base64(qr_linkedin)
image_wpp = get_base64(qr_whatsapp)

col1, col2 = st.columns(2)

col1.markdown(f'<a href="{link_url}"><img src="data:image/png;base64,{image_linkedin}" alt="linkedin" style="width: 100px; height: 100px;"/></a>', unsafe_allow_html=True)
col1.caption("Linkedin")
col2.markdown(f'<a href="{link_wpp}"><img src="data:image/png;base64,{image_wpp}" alt="linkedin" style="width: 100px; height: 100px;"/></a>', unsafe_allow_html=True)
col2.caption("Whatsapp")
