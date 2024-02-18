import streamlit as st

# Página inicial
st.title("Nome Completo")
st.write("Cientista de Dados | Resumo de qualificações")
st.markdown("[LinkedIn](link-linkedin) | [GitHub](link-github)")

# Projetos
st.header("Projetos")
projetos = [
    {
        "titulo": "Título do projeto 1",
        "descricao": "Descrição breve do projeto 1",
        "imagem": "img/logo_wpp.png",
        "link": "link-detalhes-projeto-1",
    },
    {
        "titulo": "Título do projeto 2",
        "descricao": "Descrição breve do projeto 2",
        "imagem": "img/logo_wpp.png",
        "link": "link-detalhes-projeto-2",
    },
    # ...
]

for projeto in projetos:
    st.subheader(projeto["titulo"])
    st.image(projeto["imagem"])
    st.write(projeto["descricao"])
    st.markdown(f"[Detalhes](link-{projeto['link']})")

# Habilidades
st.header("Habilidades")
habilidades = [
    {
        "nome": "Habilidade 1",
        "icone": "img/logo_wpp.png",
        "descricao": "Descrição da habilidade 1",
    },
    {
        "nome": "Habilidade 2",
        "icone": "img/logo_wpp.png",
        "descricao": "Descrição da habilidade 2",
    },
    # ...
]

for habilidade in habilidades:
    st.write(f"- {habilidade['nome']}")
    st.image(habilidade["icone"])
    st.markdown(habilidade["descricao"])

# Contato
st.header("Contato")
with st.form(key="contato"):
    nome = st.text_input("Nome")
    email = st.text_input("Email")
    mensagem = st.text_area("Mensagem")
    submit = st.form_submit_button("Enviar")

if submit:
    # Importe as bibliotecas necessárias
    import smtplib

    # Configure o servidor SMTP
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    username = "SEU_EMAIL_GMAIL"
    password = "SUA_SENHA_GMAIL"

    # Crie a mensagem
    mensagem = f"""
    Nome: {nome}
    Email: {email}
    Mensagem: {mensagem}
    """

    # Crie o objeto da mensagem
    msg = smtplib.MIMEText(mensagem)
    msg["Subject"] = "Contato via Portfólio"
    msg["From"] = username
    msg["To"] = username

    # Conecte-se ao servidor SMTP
    with smtplib.SMTP(smtp_server, smtp_port) as smtp:
        smtp.starttls()
        smtp.login(username, password)
        smtp.sendmail(username, username, msg.as_string())

    # Exiba uma mensagem de sucesso
    st.success("Mensagem enviada com sucesso!")

st.markdown("Obrigado pelo seu interesse!")