import streamlit as st
import numpy as np
import pandas as pd
import time

st.title("Forms")
st.header("Button")
clicado = st.button("Clique aqui!")

if clicado:
    st.text("Botão Clicado")


st.header("Radio")
visualizacao = st.radio("Visualização: ", ["Altair", "Plotly"])
st.text(f"Visualização: {visualizacao}")
if visualizacao == "Altair":
    st.text("Altair")
else:
    st.text("Plotly")

st.header("Checkbox")
altair_vis = st.checkbox("Visualização Altair")
plotly_vis = st.checkbox("Visualização Plotly")
st.text(f"Visualizações: {'Altair' if altair_vis else ''}, {'Plotly' if plotly_vis else ''}")

st.header("Selectbox")
visualizacao = st.selectbox("Visualização: ", ["Altair", "Plotly"])
st.write(f"Visualização: {visualizacao}")

st.header("Multiselect")
visualizacao_list = st.multiselect("Visualizações: ", ["Altair", "Plotly", "Matplotlib"], placeholder="Teste")
st.write("Visualizações: ", ", ".join(visualizacao_list))

st.header("Downloads")
X = np.linspace(1,10, 100)
quadratica = X ** 2
cubica = X ** 3
seno = np.sin(X)
tangente = np.tan(X)

polinomial = pd.DataFrame({
    'quadratica': quadratica,
    'cubica': cubica
})

trigonometrico = pd.DataFrame({
    'seno': seno,
    'tangente': tangente
})

st.download_button("Baixar Dados Polinomiais", polinomial.to_csv(), file_name='polinomial.csv')
st.download_button("Baixar Dados Trigonométricos", trigonometrico.to_csv(), file_name='trigonometrico.csv')

st.header("Barra de Progresso")
barra = st.progress(0, "Progresso: ", 200)
for i in range(0, 105, 5):
    # time.sleep(0.5)
    barra.progress(i, 'Progresso: ', 200)
st.text('Após a barra')

st.header("Spinner")
with st.spinner("Aguardando...", show_time=True, width=200):
    time.sleep(0.1)
st.text("Após o spinner")

st.header("Text Input")
nome = st.text_input("Nome:", placeholder="Digite o nome...")
senha = st.text_input("Senha:", max_chars=8, type='password', placeholder="Digite a senha...")

if nome and senha:
    st.text(f"{nome} e {senha}")
else:
    st.text("Nome e senha obrigatórios!")

st.header("Text Area")
comentario = st.text_area("Comentário:", height=600)
if comentario:
    st.text(comentario)

st.header("Campo numérico")
numero = st.number_input("Número:", min_value=5.0, max_value=10.0, value=7.0, step=1.0)
if numero:
    st.text(f"Número digitado: {numero}")

st.header("Data")
st.subheader("Data única")
data = st.date_input("Data:", format="DD/MM/YYYY")
if data:
    st.text(f"Data digitada: {data}")

st.subheader("Intervalo de Data")
intervalo_data = st.date_input("Intervalo de data:", value=("2026-01-01", "2026-08-21"))

if intervalo_data and len(intervalo_data) == 2:
    st.write(f"Início: {intervalo_data[0]}, Fim: {intervalo_data[1]}")

st.header("Horário")
horario = st.time_input("Horário:", value="09:00")
if horario:
    st.write(f"Horário digitado: {horario}")


st.header("Cores")
cor = st.color_picker("Cor:", value="#000000")
if cor:
    st.write(f"Cor: {cor}")
    st.markdown(f"<div style='background-color: {cor}; \
                width: 100%; height: 80px; border-radius: 10px;'>\
                </div>", 
                unsafe_allow_html=True)