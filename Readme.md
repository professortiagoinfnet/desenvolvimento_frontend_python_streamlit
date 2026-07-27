# Desenvolvimento Front-End com Python e Streamlit

Repositório destinado aos materiais, exemplos, exercícios e projetos da disciplina **Desenvolvimento Front-End com Python e Streamlit**.

A disciplina apresenta o desenvolvimento de aplicações web interativas utilizando Python e a biblioteca Streamlit, com foco na criação de interfaces para análise, visualização e manipulação de dados.

## Sobre a disciplina

O Streamlit é uma biblioteca Python que permite transformar scripts de análise de dados em aplicações web interativas de forma rápida e com pouco código.

Ao longo da disciplina, serão abordados conceitos de:

* configuração do ambiente de desenvolvimento;
* criação de interfaces web com Python;
* apresentação e manipulação de dados;
* criação de gráficos e dashboards;
* desenvolvimento de formulários;
* upload e download de arquivos;
* organização de aplicações com múltiplas páginas;
* estilização de aplicações;
* versionamento com Git e GitHub;
* publicação de aplicações no Streamlit Community Cloud.

## Objetivo geral

Desenvolver aplicações web interativas utilizando Python e Streamlit, aplicando recursos de interface, visualização de dados, formulários, gerenciamento de estado, organização de layouts e publicação de aplicações.

## Competências da disciplina

### 1. Preparar o ambiente de desenvolvimento

Compreender a motivação para utilizar o Streamlit, conhecer suas principais características, compará-lo com outras ferramentas para aplicações de dados e configurar o ambiente local com Python, ambientes virtuais, IDE e instalação da biblioteca.

### 2. Desenvolver aplicações simples com Streamlit

Criar aplicações utilizando textos, Markdown, LaTeX, trechos de código, DataFrames, tabelas, métricas, objetos JSON, recursos multimídia e a função `st.write()`.

### 3. Criar visualizações de dados

Desenvolver gráficos e mapas utilizando recursos nativos do Streamlit e bibliotecas como Matplotlib, Seaborn, Altair, Plotly e PyDeck.

### 4. Criar formulários e aplicações interativas

Utilizar botões, seletores, campos de entrada, upload e download de arquivos, barras de progresso, spinners, estruturas de controle, cache e Session State.

### 5. Publicar aplicações Streamlit

Utilizar Git e GitHub para versionar projetos, criar o arquivo `requirements.txt` e publicar aplicações no Streamlit Community Cloud.

### 6. Desenvolver aplicações estilizadas e com múltiplas páginas

Organizar interfaces com containers, expanders, sidebars, abas, colunas, temas, menus de navegação, múltiplas páginas e componentes externos.

## Configuração inicial do ambiente com venv

### Windows

Criar o ambiente virtual:

```bash
python -m venv .venv
```

Ativar o ambiente virtual no PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Instalar o Streamlit:

```bash
pip install streamlit
```

Executar a aplicação de demonstração:

```bash
streamlit hello
```

### Linux ou WSL

Criar o ambiente virtual:

```bash
python3 -m venv .venv
```

Ativar o ambiente virtual:

```bash
source .venv/bin/activate
```

Instalar o Streamlit:

```bash
pip install streamlit
```

Executar a aplicação de demonstração:

```bash
streamlit hello
```

## Primeira aplicação

Crie um arquivo chamado `app.py` com o conteúdo abaixo:

```python
import streamlit as st

st.title("Desenvolvimento Front-End com Python e Streamlit")

st.write("Minha primeira aplicação Streamlit.")
```

Execute a aplicação com:

```bash
streamlit run app.py
```
