import streamlit as st
import json
import pandas as pd
import numpy as np
import time

st.header("Upload Múltiplos Arquivos")
arquivos = st.file_uploader("Carregar Arquivos", type=['csv', 'json'], accept_multiple_files=True)

if arquivos:
    for arquivo in arquivos:
        st.write(arquivo.name)
        st.write(arquivo.type)
        st.write(arquivo.size)

        if arquivo.type == "application/json":
            conteudo = json.load(arquivo)
            st.json(conteudo)
        elif arquivo.type == "text/csv":
            df = pd.read_csv(arquivo, sep=';')
            st.dataframe(df)
else:
    st.write("Nenhum arquivo foi carregado!")


def processar_csv_json(arquivo):
    if arquivo.type == "application/json":
        conteudo = json.load(arquivo)
        return conteudo
    elif arquivo.type == "text/csv":
        conteudo = pd.read_csv(arquivo, sep=';')
        return conteudo
    else:
        return None

def exibir_csv_json(conteudo, type):
    if type == "application/json":
        st.json(conteudo)
    elif type == "text/csv":
        st.dataframe(conteudo)
    else:
        st.write("Erro: Tipo não reconhecido")

    
st.header("Upload Múltiplos Arquivos com Função")
arquivos = st.file_uploader("Carregar Arquivos:", type=['json', 'csv'], accept_multiple_files=True)

if arquivos is None or len(arquivos) == 0:
    st.write("Nenhum arquivo carregado!")

for arquivo in arquivos:
    conteudo = processar_csv_json(arquivo)
    exibir_csv_json(conteudo, arquivo.type)

st.header("Stop e Rerun")
nome = st.text_input("Nome: ")
numero = st.text_input("Número: ", value=np.random.randint(1, 10))
novo_numero = st.button("Novo número")

if novo_numero:
    st.rerun()

if not nome:
    st.write("Nome é obrigatório!")
    st.stop()
st.text(f"Nome: {nome}, Número: {numero}")

@st.cache_data(ttl=5)
def carregar_csv_cache(path, sep):
    df = pd.read_csv(path, sep=sep)
    return df

def carregar_csv_normal(path, sep):
    df = pd.read_csv(path, sep=sep)
    return df

start_normal = time.time()
# df = carregar_csv_normal("HIST_PAINEL_COVIDBR_2025_Parte1_05set2025.csv", ";")
final_normal = time.time()

start_cache = time.time()
df = carregar_csv_cache("HIST_PAINEL_COVIDBR_2025_Parte1_05set2025.csv", ";")
final_cache = time.time()

st.header("Cache")
st.write(f"Decorrido normal: {final_normal - start_normal}")
st.write(f"Decorrido cache: {final_cache - start_cache}")
atualizou = st.button("Atualizar")
if atualizou:
    st.rerun()

st.header("Session State")
if "contador" not in st.session_state:
    st.session_state['contador'] = 0
if st.button("Adicionar"):
    st.session_state['contador'] += 1
st.write(st.session_state['contador'])


