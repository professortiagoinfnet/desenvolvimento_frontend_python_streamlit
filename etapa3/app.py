import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# PROCESSAMENTO
X = np.linspace(1, 4, 4)
Y = np.array([10, 20, 30, 40])
Y2 = np.array([1, 2, 3, 4])

data = np.array([X, Y, Y2]).T
df = pd.DataFrame(data, columns=["Mês", "Valor", "Valor 2"])
print(data)
print(df)


# VISUALIZAÇÃO

st.title("Visualizações com Streamlit")
c1, c2 = st.columns(2)

# Gráfico Tradicional
with c1:
    st.header("Gráfico de Barra Tradicional")
    st.bar_chart(df, x="Mês", y="Valor")

#Gráfico Empilhado
with c2: 
    st.header("Gráfico de Barra Empilhado")
    st.bar_chart(df, x="Mês", y=["Valor", "Valor 2"])

# PROCESSAMENTO
X = np.linspace(1, 100, 100)
Y = 2 * X + np.random.rand(100)
Y2=  X ** 2 + np.random.rand(100)
data = np.array([X, Y, Y2]).T
df = pd.DataFrame(data, columns=["X", "Linear", "Quadrática"])
# VISUALIZAÇÃO
st.line_chart(df, x="X", y=["Linear", "Quadrática"])

# PROCESSAMENTO
teatro_municipal = [-23.54498885706442, -46.63807856072518]
cristo_redentor = [-22.951748000723917, -43.21011169235365]
pao_de_acucar = [-22.94775301608851, -43.168910864486716]

data = np.array([teatro_municipal, cristo_redentor, pao_de_acucar])
df = pd.DataFrame(data, columns=["latitude", "longitude"])

# VISUALIZAÇÃO
st.map(df)

# PROCESSAMENTO
X = ["Notebook", "Smartphone", "Fone", "Carregador"]
Y = [5000, 4000, 400, 50]

# VISUALIZAÇÃO
fig, ax = plt.subplots()
ax.bar(X, Y)
st.pyplot(fig)

fig, ax = plt.subplots(2, 2)
ax[0, 0].bar(X, Y)
ax[0, 1].scatter(X, Y)
ax[1, 0].plot(X, Y)
ax[1, 1].hist(Y)

i = 0
for line in ax:
    for grafico in line:
        grafico.set_title("Grafico " + str(i))
        grafico.set_xticks([])
        grafico.set_yticks([])
        i += 1
st.pyplot(fig)

# PROCESSAMENTO
fig, ax = plt.subplots()
sns.set_theme(style="whitegrid")
df = sns.load_dataset("tips")
sns.scatterplot(df, x='total_bill', y='tip')
st.pyplot(fig)
# VISUALIZAÇÃO