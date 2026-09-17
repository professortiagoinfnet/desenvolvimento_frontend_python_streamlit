import streamlit as st

home = st.Page("home.py",  title="Início", icon="🏠")
analise = st.Page("./pages/Analise.py", title="Análise", icon="📊")
visao_geral = st.Page("./pages/Visao_Geral.py", title="Visão Geral", icon="⚙️")

pg =  st.navigation([home, analise, visao_geral])
pg.run()
