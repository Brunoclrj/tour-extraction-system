"""
Interface Streamlit para o Tour Extraction System
Grupo 287 - Projeto Final I2A2
"""
import streamlit as st
import pandas as pd
import json
import os
import sys
from pathlib import Path
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go

# Configuração da página
st.set_page_config(
    page_title="Tour Extraction System | iFriend",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS customizado
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #1E88E5;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="main-header">🌍 Tour Extraction System</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Sistema Inteligente de Extração de Tarifários Turísticos | iFriend x I2A2</div>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("### 📋 Sobre o Sistema")
    st.info("""
    Sistema de extração automática usando:
    - 🤖 CrewAI (Agentes)
    - 🧠 GPT-4o-mini
    - 📄 Docling (OCR)
    - 🔍 FAISS (Busca)
    """)
    
    st.markdown("---")
    st.markdown("### 👥 Grupo 287")
    st.markdown("""
    - Bruno Leão
    - Victor Hugo
    - Jander Alves
    - Gleice Kelly
    - Wagner Lemos
    """)

# Carregar resultados
results_path = "output/results/tours_extracted.json"
refined_path = "output/results/tours_extracted_refined.xlsx"

if os.path.exists(results_path):
    with open(results_path, 'r', encoding='utf-8') as f:
        json_data = json.load(f)
    
    st.success(f"✅ **{len(json_data.get('tours', []))} tours** extraídos com sucesso!")
    
    # Métricas
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("🎯 Total de Tours", len(json_data.get('tours', [])))
    
    with col2:
        if os.path.exists(refined_path):
            df = pd.read_excel(refined_path)
            cities = df['Location_Main'].nunique() if 'Location_Main' in df.columns else 0
            st.metric("🏙️ Cidades", cities)
        else:
            st.metric("🏙️ Cidades", "N/A")
    
    with col3:
        if os.path.exists(refined_path) and 'Price' in df.columns:
            avg_price = df['Price'].mean()
            st.metric("💰 Preço Médio", f"€{avg_price:.2f}")
        else:
            st.metric("💰 Preço Médio", "N/A")
    
    st.markdown("---")
    
    # Mostrar dados
    if os.path.exists(refined_path):
        st.subheader("📋 Dados Extraídos")
        st.dataframe(df, use_container_width=True, height=400)
        
        # Gráficos
        if 'Location_Main' in df.columns:
            st.subheader("📊 Tours por Cidade")
            city_counts = df['Location_Main'].value_counts().head(10)
            fig = px.bar(x=city_counts.values, y=city_counts.index, orientation='h')
            st.plotly_chart(fig, use_container_width=True)
    
    # Downloads
    st.markdown("---")
    st.subheader("📥 Downloads")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        with open(results_path, 'rb') as f:
            st.download_button("📄 JSON", f, "tours.json", "application/json")
    
    with col2:
        xlsx_path = "output/results/tours_extracted.xlsx"
        if os.path.exists(xlsx_path):
            with open(xlsx_path, 'rb') as f:
                st.download_button("📊 Excel", f, "tours.xlsx")
    
    with col3:
        if os.path.exists(refined_path):
            with open(refined_path, 'rb') as f:
                st.download_button("✨ Excel Refinado", f, "tours_refined.xlsx")

else:
    st.warning("⚠️ Nenhum resultado encontrado. Execute o processamento primeiro!")
    st.code("python main.py --pdf 'input/PRIVATE_TOURS_FRANCE_2024-EN.pdf'")

