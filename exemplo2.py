import streamlit as st
import io
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from nltk.corpus import stopwords
from PIL import Image, ImageChops
import nltk

# Carreguando o ícone da aba
favicon = "img/dados.png"

# Configurações da página Streamlit
st.set_page_config(page_title="Nuvem de Palavras", page_icon=favicon)

# Define o banner
banner_image = "img/banner.jpeg"

# Adiciona o banner ao aplicativo
st.image(banner_image, use_column_width=True)

def gerar_nuvem_palavras(texto):
  """
  Gera uma nuvem de palavras a partir de um texto e retorna um buffer em memória.

  Argumentos:
    texto: String contendo o texto a ser usado na nuvem de palavras.

  Retorno:
    Buffer em memória contendo a imagem da nuvem de palavras em formato PNG.
  """

  stop_words = set(stopwords.words('portuguese'))

  # Gerando a nuvem de palavras
  wordcloud = WordCloud(
      background_color="black",
      stopwords=stop_words,
      max_words=qtde_palavras,
      max_font_size=100,
      random_state=42,
      margin=0
  ).generate(texto)

  def trim(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)

  image = wordcloud.to_image()
  image = trim(image)

  # Plotando a nuvem de palavras
  plt.figure(figsize=(8, 4))
  plt.imshow(image, interpolation="bilinear")
  plt.axis("off")

  # Salvando a nuvem de palavras em um buffer em memória
  buffer = io.BytesIO()
  plt.savefig(buffer, format="png", bbox_inches="tight", pad_inches=0.1)
  buffer.seek(0)

  return buffer

# Interface do Streamlit
st.title("Nuvem de palavras")

st.subheader("Insira o texto que deseja usar para gerar a nuvem de palavras:")

# Entrada de texto
texto = st.text_area("Texo:", height=100)

# Quantidade de palavras
qtde_palavras = st.number_input("Quantidade de palavras:", min_value=1, max_value=200, value=60)

# Gerando a nuvem de palavras
if st.button("Gerar nuvem de palavras"):
  buffer = gerar_nuvem_palavras(texto)

  # Exibindo a nuvem de palavras
  st.image(buffer, use_column_width=True)

  # Permitindo o download da imagem
  st.download_button(
      label="Baixar imagem da nuvem de palavras",
      data=buffer,
      file_name='wordcloud.png',
      mime='image/png'
  )
print(nltk.data.path)