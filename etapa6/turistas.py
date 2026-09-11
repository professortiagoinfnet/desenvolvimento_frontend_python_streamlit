import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

colunas = ['Continente/Pais', 'Total', 'Janeiro',	'Fevereiro',	'Março',	'Abril', 'Maio',
           	'Junho',	'Julho',	'Agosto',	'Setembro',	'Outubro',	'Novembro',	'Dezembro']

df = pd.read_excel("2676.xls", header=None, skiprows=7)
df = df.iloc[0:63,:]
df = df.drop(0)
df.columns = colunas
df = df.drop('Total', axis=1)
df = df.drop([1, 7, 12, 16, 29, 34, 54, 57])
df = df.replace('-', 0)
# print(df.iloc[30:70,:])

for col in df:
    if col != 'Continente/Pais':
        df[col] = df[col].astype('int')

df.loc[6, 'Continente/Pais'] = "Outros África"
df.loc[11, 'Continente/Pais'] = "Outros América Central"
df.loc[33, 'Continente/Pais'] = "Outros Ásia"
df.loc[53, 'Continente/Pais'] = "Outros Europa"
df.loc[61, 'Continente/Pais'] = "Outros Oriente Médio"

fig, ax = plt.subplots()
(n, m) = df.shape
for i in range(n):
    linha = df.iloc[i, 1:]
    X = linha.index.values
    Y = linha.values
    ax.plot(X, Y, label=df.iloc[i, 0])
ax.legend()
st.pyplot(fig)
print(df)