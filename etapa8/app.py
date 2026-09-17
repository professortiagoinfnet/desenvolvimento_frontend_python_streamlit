import streamlit as st
import time
import numpy as np
import pandas as pd
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


Y2 = np.exp(X)
df = pd.DataFrame({"X": X, "Y": Y, "Y2": Y2})

st.title("Colunas")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Média Y", df['Y'].mean())
c2.metric("Média Y2", df['Y2'].mean())
c3.metric("Max Y", df['Y'].max())
c4.metric("Max Y2", df['Y2'].max())

st.header("Colunas Proporcionais")
esq, dir = st.columns((2, 1))
esq.line_chart(df, x='X', y='Y')
dir.line_chart(df, x='X', y='Y2')

st.header("Grid")
produtos = ['A', 'B', 'C', 'D', 'E', 'F']

for i in range(0, 2):
    colunas = st.columns(3)
    for j in range(3):
        p = i * 3 + j
        colunas[j].metric("Produto", produtos[p])


st.title("Tabs")
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun']
vendas = [10, 30, 15, 2, 5, 6]
df = pd.DataFrame({'Mes': meses, 'Venda': vendas})
print(df)

tab1, tab2, tab3 = st.tabs(['Resumo', 'Gráficos', 'Dados'])

with tab1:
    st.metric("Total", df['Venda'].sum())
    st.metric("Média", df['Venda'].mean())

with tab2:
    st.line_chart(df, x="Mes", y="Venda")

with tab3:
    st.dataframe(df)