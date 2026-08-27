import streamlit as st
import altair as alt
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots

## PROCESSAMENTO
cars = alt.datasets.data.cars()

## VISUALIZAÇÃO

# Generate Altair plots
grafico1 = alt.Chart(cars).mark_line().encode(
    x="Miles_per_Gallon",
    y="Weight_in_lbs"
)

grafico2 = alt.Chart(cars).mark_bar().encode(
    x="Weight_in_lbs",
    y="Acceleration"
)

grafico3 = alt.Chart(cars).mark_area().encode(
    x="Horsepower",
    y="Acceleration"
)

# Streamlit visualization
st.title("Gráficos Altair")
st.header("Gráfico Univariável")
c1, c2, c3 = st.columns(3)
with c1:
    st.altair_chart(grafico1)

with c2:
    st.altair_chart(grafico2)

with c3:
    st.altair_chart(grafico3)

# print(cars.head())


## PROCESSAMENTO
cars = alt.datasets.data.cars()
cars = cars.reset_index()

## VISUALIZAÇÃO

# Generate Altair plots
grafico1 = alt.Chart(cars).transform_calculate(serie="'Horsepower'").mark_line().encode(
    x="index",
    y="Horsepower",
    color="serie:N"
)

grafico2 = alt.Chart(cars).transform_calculate(serie="'Weight_in_lbs'").mark_line().encode(
    x="index",
    y="Weight_in_lbs",
    color="serie:N"
)

grafico3 = grafico1 + grafico2


# Streamlit Visualization
st.header("Gráfico Multivariáveis")
st.altair_chart(grafico3)


gapminder = alt.datasets.data.gapminder()
gapminder_2000 = gapminder[gapminder['year'] == 2000]

grafico = alt.Chart(gapminder_2000).mark_circle().encode(
    x="fertility",
    y="life_expect",
    color="cluster:N",
    size="pop:Q"
)
st.header("Gráfico Multidimensões")
st.altair_chart(grafico)
print(gapminder_2000)


## PROCESSAMENTO
penguins = alt.datasets.data.penguins()
grafico = alt.Chart(penguins).mark_boxplot().encode(
    x=alt.X("Body Mass (g)", scale=alt.Scale(domain=[2500, 6500])),
    y=alt.Y("Beak Length (mm)", scale=alt.Scale(domain=[30, 60]))
)


## VISUALIZAÇÃO

st.header("Boxplot")
st.altair_chart(grafico)

## PROCESSAMENTO
penguins = penguins.dropna()
print(penguins)

## VISUALIZAÇÃO

heatmap1 = alt.Chart(penguins).mark_rect().encode(
    x='Species:N',
    y='Island:N',
    color='count():Q'
)

heatmap2 = alt.Chart(penguins).mark_rect().encode(
    x='Species:N',
    y='Sex:N',
    color='sum(Body Mass (g)):Q'
)

st.header("Heatmap")
st.altair_chart(heatmap1)
st.altair_chart(heatmap2)

## PROCESSAMENTO
df = pd.DataFrame({
    "mes": [
        "Jan", "Fev", "Mar", "Abr", "Mai", "Jun",
        "Jan", "Fev", "Mar", "Abr", "Mai", "Jun",
        "Jan", "Fev", "Mar", "Abr", "Mai", "Jun"
    ],
    "produto": [
        "Notebook", "Notebook", "Notebook", "Notebook", "Notebook", "Notebook",
        "Monitor", "Monitor", "Monitor", "Monitor", "Monitor", "Monitor",
        "Mouse", "Mouse", "Mouse", "Mouse", "Mouse", "Mouse"
    ],
    "vendas": [
        40, 45, 52, 55, 63, 70,
        30, 34, 38, 41, 45, 49,
        80, 90, 95, 110, 120, 130
    ],
    "preco": [
        3500.0, 3500.0, 3500.0, 3500.0, 3500.0, 3500.0, 
        1200.0, 1200.0, 1200.0, 1200.0, 1200.0, 1200.0, 
        200.0 , 200.0 , 200.0 , 200.0 , 200.0 , 200.0 
    ]
    
})

df_grouped = df.groupby('produto')['vendas'].sum()
df_vendas_por_produto = df_grouped.reset_index()

## VISUALIZAÇÃO

fig_pie = px.pie(df_vendas_por_produto,
                 names='produto',
                 values='vendas')

fig_donut = px.pie(df_vendas_por_produto,
                   names='produto',
                   values='vendas',
                   hole=0.5)

st.title('Plotly')
st.header('Pie e Donut')
st.plotly_chart(fig_pie)
st.plotly_chart(fig_donut)

## PROCESSAMENTO
df['receita'] = df['vendas'] * df['preco']
df['receita percentual'] = df['receita'] / df['receita'].sum() * 100
df_notebook = df[df['produto'] == "Notebook"]
df_monitor = df[df['produto'] == "Monitor"]
df_mouse = df[df['produto'] == "Mouse"]

print(df_notebook)
print(df_monitor)
print(df_mouse)
print(df)

fig_line = px.line(df_notebook,
                   x='mes',
                   y='vendas',
                   markers=True)

fig_line2 = px.line(df_notebook,
                    x='mes',
                    y=['vendas', 'receita percentual'],
                    markers=True)

fig_line3 = px.line(df,
                    x='mes',
                    y='vendas',
                    markers=True,
                    color='produto')

st.plotly_chart(fig_line)
st.plotly_chart(fig_line2)
st.plotly_chart(fig_line3)

## PROCESSAMENTO

## VISUALIZAÇÃO
fig_bar = px.bar(df_vendas_por_produto,
                 y='produto',
                 x='vendas',
                 color='produto',
                 text='vendas',
                 orientation='h')

fig_bar2 = px.bar(df_notebook,
                  x='mes',
                  y=['vendas', 'receita percentual'],
                  barmode='group'
                  )

st.header('Bar')
st.plotly_chart(fig_bar)
st.plotly_chart(fig_bar2)


## PROCESSAMENTO
print(df_notebook)
print(df_mouse)

## VISUALIZAÇÃO

fig1 = px.line(df_notebook,
               x='mes',
               y='vendas',
               title='Notebook')

fig2 = px.bar(df_mouse,
              x='mes',
              y='vendas',
              title='Mouse')

fig_subplot = make_subplots(rows=1, cols=2)

for trace in fig1.data:
    fig_subplot.add_trace(trace, row=1, col=1)

for trace in fig2.data:
    fig_subplot.add_trace(trace, row=1, col=2)

st.plotly_chart(fig_subplot)

## PYDECK
import pydeck as pdk

df_rio = pd.DataFrame({
    'local': ["Igreja Candelária"],
    'latitude': [-22.90049674395883],
    'longitude': [-43.17700158812346]
    })

rio_initial_view = pdk.ViewState(
    latitude=df_rio.loc[0,'latitude'],
    longitude=df_rio.loc[0, 'longitude'],
    zoom=20,
    pitch=0,
    bearing=100
)

deck = pdk.Deck(
    initial_view_state=rio_initial_view
)
st.header("Mapa com PyDeck")
st.pydeck_chart(deck)

df_rio = pd.DataFrame({
    'local': ["Candelária", "São Bento", "Aeroporto", "Teatro"],
    'latitude': [-22.90049674395883, -22.896810496584695, -22.909174243762013, -22.908860278878034],
    'longitude': [-43.17700158812346, -43.17742651959921, -43.16260433162997, -43.17599960142952],
    'valor': [100, 200, 300, 400]
    })
print(df_rio)

rio_initial_view = pdk.ViewState(latitude=df_rio.loc[1,'latitude'], longitude=df_rio.loc[1, 'longitude'],
    zoom=15,
    pitch=180,
    bearing=100
)

layer1 = pdk.Layer("ScatterplotLayer", data=df_rio, get_position=["longitude", "latitude"], get_radius='valor')

layer2 = pdk.Layer("ColumnLayer", data=df_rio, get_position=["longitude", "latitude"], radius=200, opacity=0.5)

deck = pdk.Deck(initial_view_state=rio_initial_view, layers=[layer1])
st.header("Mapa com PyDeck")
st.pydeck_chart(deck)

