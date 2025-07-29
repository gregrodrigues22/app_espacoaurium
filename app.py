import streamlit as st
import pandas as pd
import os

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
df = carregar_dados()

st.header("🎲 Tipos de Análise")

# --- SELEÇÃO DE TIPO DE ANÁLISE ---
aba = st.tabs([
    "🧑 Clientes",
    "🤝 Parceiros",
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

with aba[1]:
    st.info("Conteúdo de Análise de Parceiros — (em construção)")

with aba[2]:
    st.info("Conteúdo de Análise de Satisfação — (em construção)")

with aba[3]:
    st.info("Conteúdo de Análise Financeira — (em construção)")

    