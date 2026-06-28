
import streamlit as st
import os

# --- CONFIGURAÇÃO DA SKIN (CSS) ---
def local_css():
    st.markdown("""
    <style>
    .block-container { padding-top: 2rem; max-width: 800px; }
    div.stButton > button {
        width: 100%; height: 50px; border-radius: 10px; font-weight: bold;
    }
    .stTextArea textarea { border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

local_css()

# --- TELA PRINCIPAL ---
st.title("🎨 Gerador Criativo AI")
st.markdown("Crie projetos com qualidade profissional.")

tab1, tab2 = st.tabs(["🖼️ Gerar Imagem", "🎥 Gerar Vídeo"])

# --- LÓGICA DE GERAÇÃO COM CHAVES ÚNICAS ---
def render_gerador(tipo, key_prefix):
    st.subheader(f"Configurações de {tipo}")
    
    # Adicionamos 'key' única baseada no prefixo para cada widget
    modelo = st.selectbox(f"Modelo de {tipo}", ["Flux 1.1 Pro", "SDXL", "DALL-E 3"], key=f"modelo_{key_prefix}")
    
    prompt = st.text_area("Descreva seu projeto:", placeholder="Ex: Uma paisagem futurista...", key=f"prompt_{key_prefix}")
    
    uploaded_files = st.file_uploader("Arraste até 5 imagens", accept_multiple_files=True, type=['png', 'jpg'], key=f"upload_{key_prefix}")
    
    proporcao = st.radio("Formato:", ["1:1", "9:16", "16:9"], horizontal=True, key=f"prop_{key_prefix}")
    
    if st.button(f"🚀 GERAR {tipo.upper()}", key=f"btn_gerar_{key_prefix}", use_container_width=True):
        if not prompt:
            st.error("Escreva um prompt!")
        else:
            st.success(f"Processando {tipo}...")

with tab1:
    render_gerador("Imagem", "img")

with tab2:
    render_gerador("Vídeo", "vid")

# --- PAINEL DE LOTE ---
with st.expander("📦 Fila de Produção"):
    st.write("Fila vazia.")
