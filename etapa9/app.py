import seaborn as sns
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt

st.title("Gráfico de Seleção de Ponto Bidirecional")

df = sns.load_dataset('penguins')
fig = px.scatter(df, x='bill_length_mm', y='bill_depth_mm', color='species')
event = st.plotly_chart(fig, on_select='rerun', selection_mode='points')

st.subheader("Ponto Selecionado:")
st.write(event.selection.points)

st.title("Gráfico de Seleção Retangular e Área Livre Bidirecional")
df = sns.load_dataset('penguins')
fig = px.scatter(df, x='body_mass_g', y='flipper_length_mm', color='island')
event = st.plotly_chart(fig, on_select='rerun', selection_mode=['lasso', 'box'])
st.subheader("Pontos Selecionados:")

X = []
Y = []
for point in event.selection.points:
    X.append(point['x'])
    Y.append(point['y'])

fig, ax = plt.subplots()
ax.scatter(X, Y)
st.pyplot(fig)

st.subheader("Geometria do lasso:")
if event.selection.lasso:
    st.write(event.selection.lasso)

st.subheader("Geometria do box")
if event.selection.box:
    st.write(event.selection.box)

st.title("Drill-Down")

df = sns.load_dataset('penguins')
df = df.dropna().reset_index()

fig = px.scatter(df, x='bill_length_mm', y='bill_depth_mm', color='species', custom_data=['index'])
event = st.plotly_chart(fig, on_select='rerun', selection_mode='points')

st.subheader("Exemplo selecionado:")
if len(event.selection.points) > 0:
    index = event.selection.points[0]['customdata']['0']
    line = df[df['index'] == index]
    st.dataframe(line)
