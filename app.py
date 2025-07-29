# ---------------------------------------------------------------
# Set up
# ---------------------------------------------------------------
import streamlit as st  
import plotly.graph_objects as go
import numpy as np
from google.cloud import bigquery
import pandas as pd
import json
from scipy.stats import linregress
from plotly.subplots import make_subplots
from plotly.colors import sequential
import os

# ---------------------------------------------------------------
# Big Query
# ---------------------------------------------------------------
PROJECT_ID = "escolap2p" 
TABLE_ID = "escolap2p.cliente_espacoaurium.crm" 

with open("/tmp/keyfile.json", "w") as f:
    json.dump(st.secrets["bigquery"].to_dict(), f)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/tmp/keyfile.json"

client = bigquery.Client()

# ---------------------------------------------------------------
# Aquisição de dados do Big Query
# ---------------------------------------------------------------
@st.cache_data
def consultar_dados():
    client = bigquery.Client()
    query = """
        SELECT
            *
        FROM
            `escolap2p.cliente_espacoaurium.crm`
    """
    return client.query(query).to_dataframe()

# Executa a query e transforma em DataFrame
df = consultar_dados()

# ---------------------------------------------------------------
# Configuração da página
# ---------------------------------------------------------------
st.set_page_config(layout="wide", page_title="📊 Painel Espaço Aurium")

# ---------------------------------------------------------------
# Side bar
# ---------------------------------------------------------------
with st.sidebar:
    st.image("assets/logo.jpg", use_container_width=True)
    st.markdown("""
        <div style='margin: 20px 0;'>
            <hr style='border: none; border-top: 1px solid #ccc;' />
        </div>
    """, unsafe_allow_html=True)
    st.header("Menu")
    st.page_link("app.py", label="Análise", icon="📊")
    st.page_link("pages/criacao.py", label="Referência", icon="✅")
    st.markdown("""
        <div style='margin: 20px 0;'>
            <hr style='border: none; border-top: 1px solid #ccc;' />
        </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------------
# Cabecalho
# ---------------------------------------------------------------
st.markdown("""
    <div style='background: linear-gradient(to right, #004e92, #000428); padding: 40px; border-radius: 12px; margin-bottom:30px'>
        <h1 style='color: white;'>📊 Análise Espaço Aurium</h1>
        <p style='color: white;'>Explore os dados da Clínica Espaço Aurium escolhendo a métrica e aplicando filtros nas dimensões.</p>
    </div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------
# Carregando dos dados
# ---------------------------------------------------------------

st.header("🎲 Tipos de Análise")

# --- SELEÇÃO DE TIPO DE ANÁLISE ---
aba = st.tabs([
    "🧑 Clientes",
    "🤝 Parceiros",
    "🛒 Vendas",
    "📊 Satisfação",
    "💰 Financeiro"
])

# ────────────────────────────────────────────────────────────────────────────────
#  ABA 0  –  Análise por Colaboradores
# ────────────────────────────────────────────────────────────────────────────────

with aba[0]:

    # --- Título e preparação ----------------------------------------------------------
    st.subheader("🧑 Clientes")
    st.info("Conteúdo de Análise de Clientes — (em construção)")

# ────────────────────────────────────────────────────────────────────────────────
#  ABA 1  –  Análise por Parceiros
# ────────────────────────────────────────────────────────────────────────────────

with aba[1]:
    st.subheader("🤝 Parceiros")
    st.info("Conteúdo de Análise de Parceiros — (em construção)")

# ────────────────────────────────────────────────────────────────────────────────
#  ABA 0  –  Análise por Vendas
# ────────────────────────────────────────────────────────────────────────────────

with aba[2]:
    st.subheader("🛒 Vendas")

    # Painel com filtros
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        etapa = st.selectbox("Etapas", options=["Todos"] + sorted(df['etapa'].dropna().unique().tolist()))

    with col2:
        status = st.multiselect("Status", options=sorted(df['status'].dropna().unique()))

    with col3:
        perda = st.multiselect("Razão de perda", options=sorted(df['loss_reason'].dropna().unique()))

    with col4:
        ganho = st.multiselect("Razão de ganho", options=sorted(df['gain_reason'].dropna().unique()))

# ────────────────────────────────────────────────────────────────────────────────
#  ABA 0  –  Análise por Vendas
# ────────────────────────────────────────────────────────────────────────────────

with aba[3]:
    st.subheader("📊 Satisfação")
    st.info("Conteúdo de Análise de Satisfação — (em construção)")

with aba[4]:
    st.subheader("💰 Financeiro")
    st.info("Conteúdo de Análise Financeira — (em construção)")

    