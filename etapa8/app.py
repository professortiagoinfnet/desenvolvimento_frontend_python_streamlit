import streamlit as st
import time
import numpy as np
import matplotlib.pyplot as plt

st.title("Container")

container = st.container()

st.header("Produto:")
produto = st.selectbox("Selecionar o produto:", ['Mouse', 'Teclado', 'Monitor', 'Notebook'])
preco = st.number_input("Digite o preço", min_value=0.01)
quantidade = st.number_input("Digite a quantidade", min_value=1)
total = preco * quantidade

with container:
    st.header("Resumo:")
    st.write(f"Produto: {produto}")
    st.write(f"Preço: {preco}")
    st.write(f"Quantidade: {quantidade}")
    st.write(f"Total: {total}")

st.title("Empty")
st.header("Contador Dinâmico")
contador_dinamico = st.empty()

for i in range(5, 0, -1):
    # contador_dinamico.write(f"Começa em {i} segundos")
    with contador_dinamico:
        st.write(f"Começa em {i} segundos")
    # time.sleep(1)

contador_dinamico.success("Iniciado!")

st.header("Gráfico Dinâmico")
grafico_dinamico = st.empty()

X = np.linspace(-5, 5, 100)
Y = X ** 2

# for i in range(0, 100):
#     with grafico_dinamico:
#         fig, ax = plt.subplots()
#         ax.plot(X[0:i+1], Y[0:i+1], marker='o')
#         ax.set_xlim((-5, 5))
#         ax.set_ylim((0, 25))
#         st.pyplot(fig)
#         time.sleep(0.2)

st.title("Expander")
with st.expander("Estatísticas do gráfico dinâmico"):
    st.write(f"Média: {Y.mean()}")
    st.write(f"Variância: {Y.var()}")
    st.write(f"Soma: {Y.sum()}")

st.expander("Média * Soma:").write(f"Média * soma: {Y.mean() * Y.sum()}")

st.title("Sidebar")
st.sidebar.header("Filtros")
with st.sidebar:
    categoria = st.selectbox("Categoria: ", ["Produtos", "Serviços"])
    preco = st.text_input("Preço Máximo:")
    st.write(f"Categoria: {categoria}")
    st.write(f"Preço: {preco}")
