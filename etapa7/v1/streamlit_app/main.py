import numpy as np
import pandas as pd
import streamlit as st
import altair as alt

X = np.linspace(-5, 5, 100)
Y_quadrado = X ** 2
Y_seno  = np.sin(2 * np.pi * X)

df = pd.DataFrame({
    "X": X,
    "Quadrado": Y_quadrado,
    "Seno": Y_seno
})

st.title("Gráfico Quadrado Seno")
grafico = alt.Chart(df).mark_circle().encode(
    x='X',
    y='Quadrado',
    size='Seno'
)

st.altair_chart(grafico)
