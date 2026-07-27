import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello World!")
st.text("Streamlit para Ciência de Dados")
st.text("Primeiro programa Streamlit")
st.text("Exemplo atualização")
st.write("Texto com write")

st.title("Formulário Usuário")
nome = st.text_input("Digite seu nome:")
idade = st.slider("Selecione sua idade:", 10, 100, 25)
salario = st.text_input("Digite o salário:")

try:
    salario = float(salario)
except:
    salario = float(-1)

if nome != "":
    st.write(f"Nome: {nome} e Idade: {idade}")

linguagem_escolhida = st.selectbox("Selecione a linguagem:", ["", "Python", "Javascript", "Rust", "C"])
if linguagem_escolhida != "":
    st.write(f"Linguagem Escolhida: {linguagem_escolhida}")

aceito = st.checkbox("Você aceita os Termos de Uso")
if aceito:
    st.write("Obrigado por aceitar!")



print("nome", type(nome), nome)
print("idade", type(idade), idade)
print("salario", type(salario), salario)
print(linguagem_escolhida)
