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
    st.markdown("<small>Indicadores com meta 0 ao final do dia</small>", unsafe_allow_html=True)

    # Painel com filtros
    #col1, col2, col3, col4 = st.columns(4)

    #with col1:
    #    etapa = st.selectbox("Etapas", options=["Todos"] + sorted(df['etapa'].dropna().unique().tolist()))

    #with col2:
    #    status = st.multiselect("Status", options=sorted(df['status'].dropna().unique()))

    #with col3:
    #    perda = st.multiselect("Razão de perda", options=sorted(df['loss_reason'].dropna().unique()))

    #with col4:
    #    ganho = st.multiselect("Razão de ganho", options=sorted(df['gain_reason'].dropna().unique()))
    
    #df_filtrado = df.copy()
    
    # Filtro por Etapa
    #if etapa != "Todos":
    #    df_filtrado = df_filtrado[df_filtrado['etapa'] == etapa]

    # Filtro por Status
    #if status:
    #    df_filtrado = df_filtrado[df_filtrado['status'].isin(status)]

    # Filtro por Razão de Perda
    #if perda:
    #    df_filtrado = df_filtrado[df_filtrado['loss_reason'].isin(perda)]

    # Filtro por Razão de Ganho
    #if ganho:
    #    df_filtrado = df_filtrado[df_filtrado['gain_reason'].isin(ganho)]

    # Exibir métricas em linha (dividido em duas linhas de 3 colunas)
    col1, col2, col3 = st.columns(3)

    with col1:
        meta_1 = df[df['etapa'] == "Novo Lead"]
        st.metric("Cartões na Etapa Novo Lead", len(meta_1))
    
    with col2:
        meta_2 = df[df['etapa'] == "Contato inicial"]
        st.metric("Cartões na Etapa Contato inicial", len(meta_2))
    
    with col3:
        etapas_meta_3 = ["Breakup", "Agendado", "Reativação de Venda Perdida","Finalização para Pós Venda"]
        meta_3 = df[(df['etapa'].isin(etapas_meta_3)) & (df['status'] == "open")]
        st.metric("Status Aberto nas Etapas 'Agendado', 'Reativação Perdida' e 'Finalização Pós Venda'", len(meta_3))

    col4, col5, col6 = st.columns(3)
    
    with col4:
        etapas_finais = ["Agendado", "Finalização para Pós Venda", "Avanço para Proposta Procedimento"]
        meta_4 = df[(df['status'] == "gain") & (~df['etapa'].isin(etapas_finais))]
        st.metric("Ganho fora das Etapas 'Agendado', 'Finalização Pós Venda' e 'Avanço Procedimento'", len(meta_4))

    with col5:
        meta_5 = df[(df['status'] == "lost") & (~df['etapa'].isin(["Breakup", "Reativação de Venda Perdida"]))]
        st.metric("Perdido fora das Etapas 'Breakup' e 'Reativação Perdida'", len(meta_5))

    with col6:
        meta_6 = df[(df['etapa'] == "Agendado") & ( (df['value'] == '0.00') | (df['fields_Produto'].isna()) )]
        st.metric("Agendado com Informação Incompleta", len(meta_6))

# ────────────────────────────────────────────────────────────────────────────────
#  ABA 0  –  Análise por Vendas
# ────────────────────────────────────────────────────────────────────────────────

with aba[3]:
    st.subheader("📊 Satisfação")
    st.info("Conteúdo de Análise de Satisfação — (em construção)")

with aba[4]:
    st.subheader("💰 Financeiro")
    st.info("Conteúdo de Análise Financeira — (em construção)")

    