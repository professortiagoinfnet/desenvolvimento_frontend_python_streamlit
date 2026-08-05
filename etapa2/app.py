import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

st.header("Exemplo de Título")

st.subheader("Exemplo de Subtítulo")

st.caption("Exemplo de legenda")

st.text("Exemplo de texto")

st.title("Colunas")

st.header("Duas Colunas")
col1, col2 = st.columns(2)

with col1:
    st.write("Essa é a Coluna 1")
    st.caption("C1")
    arquivo = st.file_uploader("Anexe o arquivo desejado:", type=['csv'])
    if arquivo:
        st.write(f"Nome: {arquivo.name}")
        st.write(f"Tipo: {arquivo.type}")
        st.write(f"Tamanho: {arquivo.size}")

        df = pd.read_csv(arquivo)
        st.dataframe(df)

with col2:
    st.write("Essa é a Coluna 2")
    st.caption("C2")

st.header("Quatro Colunas")
c1, c2, c3, c4 = st.columns(4)
c1.write("C1")
c2.write("C2")
c3.write("C3")
c4.write("C4")

st.header("Texto em Markdown")
st.markdown("# Texto 1")
st.markdown("## Texto 2")
st.markdown("### **Texto 3**")

st.header("Texto em Latex")
st.latex("""f(x_i, x_j) = x_i^2 + x_j^3""")
st.latex(r'''\theta = \alpha + \beta''')

st.header("Texto de Código-Fonte")
st.code("""
    def quadrado(x):
        return x ** 2
""", language="python")

st.code("""
    int main(int argc, char *argv[]){
        return 0;    
    }
        """, language="c")

st.header("DataFrame Pandas")
idades = [15, 30, 25, 26]
nomes = ["Maria", "José", "Pedro", "Lucas"]

df = pd.DataFrame(data={"Nome": nomes, "Idade": idades})
print(df)
st.dataframe(df)
st.dataframe(df.head(2))

st.header("Função Dataframe vs função table")

matriz = np.random.randn(30, 10)
df = pd.DataFrame(data=matriz)

st.subheader("Dataframe")
st.dataframe(df)
st.dataframe(df.style.highlight_min().highlight_max())

st.subheader("Table")
st.table(matriz)

st.subheader("Metric")
st.metric(label="Temperatura", value="35C", delta="+1", delta_color="off")

c1, c2, c3 = st.columns(3)
with c1:
    st.metric("Altitude", value="100m", delta='-5m')

c2.metric("Tempo de Execução médio", value="10s", delta='3ms')
c3.metric("Uso de memória", value="1.5GB", delta="100MB")

st.subheader("Json")
st.json(
    {
        "Books": [
            {
                "Nome": "Crime e Castigo",
                "Autor": "Fiódor Dostoiévski",
                "Ano": '1866'
             },
             {
                "Nome": "Memórias Póstumas de Braz Cubas",
                "Autor": "Machado de Assis",
                "Ano": "1881"
             }
        ]
    }
)

st.subheader("Write como superfunção")

X = np.linspace(0, 5, 100)
Y_quadrado = X ** 2
Y_exponencial = np.exp(X)
Y_linear = X * 10

df_funcoes = pd.DataFrame(
    {
        "Quadratica": Y_quadrado,
        "Exponencial": Y_exponencial,
        "Linear": Y_linear})

plt.plot(X, Y_quadrado, label="quadrática")
plt.plot(X, Y_exponencial, label="exponencial")
plt.plot(X, Y_linear, label="linear")
plt.title("Exemplos de funções")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
st.write(plt.gcf())
st.subheader("Dados das funções:")
st.write(df_funcoes)

st.subheader("Magic")
"Soma = 5 + 4", 5 + 4
st.write("Soma = 5 + 4", 5 + 4)

"""
# Título Markdown
## Subtítulo Markdown
"""

st.subheader("Imagens")
st.image("118-1024x768.jpg", width="stretch", caption="Imagem Picsum")

imagem = Image.open("118-1024x768.jpg")
st.image(imagem)

st.subheader("Audio")
st.audio("https://samplelib.com/mp3/sample-3s.mp3")

f = open("sample-3s.mp3", "rb")
audio_bytes = f.read()
st.audio(audio_bytes)

st.subheader("Video")
st.video("https://samplelib.com/mp4/sample-5s.mp4")

f = open("sample-5s.mp4", "rb")
video_bytes = f.read()
st.video(video_bytes)

st.subheader("Animações")

if st.text_input("Digite Ok") == "Ok":
    st.balloons()
    st.snow()

st.set_page_config(page_title="Meu Dashboard", page_icon=":bar_chart:")
st.write(":streamlit:")