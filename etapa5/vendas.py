import pandas as pd
import streamlit as st
import plotly.express as px


df = pd.read_csv("train.csv")
regioes = df['Region'].unique().tolist()
opcoes_regioes = regioes + ['Todos']
st.dataframe(df)
regiao = st.selectbox("Regiões", opcoes_regioes)
df_filtrado_by_regiao = df[df['Region'] == regiao]
total_vendas_by_regiao = df_filtrado_by_regiao['Sales'].sum()
total_vendas = df['Sales'].sum()

vendas_by_regiao = df_filtrado_by_regiao[['Row ID', 'Sales']]
vendas = df[['Row ID', 'Sales']]

st.header("Total:")
if regiao == "Todos":
    st.write(f"Total vendas: {total_vendas}")
else:
    st.write(f"Total vendas {regiao}: {total_vendas_by_regiao}")
print(df.columns)
st.header("Evolução")
if regiao == "Todos":
    grafico = px.line(vendas, x="Row ID", y="Sales")
else:
    grafico = px.line(vendas_by_regiao, x="Row ID", y="Sales")

st.plotly_chart(grafico)
print(regiao)
print(vendas_by_regiao)