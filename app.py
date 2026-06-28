
import streamlit as st
import requests
import os

# --- 1. CONFIGURAÇÃO VISUAL (SKIN ESCURA IGUAL À IMAGEM) ---
st.set_page_config(page_title="Gerador Pro AI", layout="centered")

st.markdown("""
    <style>
    /* Fundo escuro global */
    .stApp { background-color: #0e1117; color: white; }
    
    /* Ajuste da área principal */
    .block-container { padding-top: 2rem; }
    
    /* Caixa de Upload */
    .stFileUploader { background-color: #1e1e26; border-radius: 10px; padding: 15px; }
    
    /* Caixa de Texto */
    .stTextArea textarea { background-color: #1e1e26; color: white; border: 1px solid #333; border-radius: 10px; height: 150px; }
    
    /* Botão Gerar */
    div.stButton > button { 
        background-color: #1e1e26; color: white; border: 1px solid #444; 
        border-radius: 8px; height: 3em; width: 100%; font-weight: bold;
    }
    div.stButton > button:hover { border-color: #ff4b4b; color: #ff4b4b; }
    </style>
""", unsafe_allow_html=True)

# --- 2. LÓGICA DO APP ---
st.title("🎨 Gerador Criativo AI")

tab1, tab2 = st.tabs(["🖼️ Gerar Imagem", "🎥 Gerar Vídeo"])

def processar_geracao(tipo, key_prefix):
    st.subheader(f"Configurações de {tipo}")
    
    # Upload de referências
    uploaded_files = st.file_uploader(f"Carregar até 5 referências", accept_multiple_files=True, key=f"up_{key_prefix}")
    
    # Grid de miniaturas das referências
    if uploaded_files:
        cols = st.columns(5)
        for i, file in enumerate(uploaded_files[:5]):
            cols[i].image(file, use_container_width=True)
            
    # Prompt
    prompt = st.text_area("Descreva seu projeto:", key=f"prompt_{key_prefix}")
    
    # Botão Gerar
    if st.button(f"🚀 GERAR {tipo.upper()}", key=f"btn_{key_prefix}"):
        if not prompt:
            st.warning("Por favor, digite um prompt.")
        else:
            with st.spinner("IA processando..."):
                # AQUI ENTRA A CHAMADA DA SUA API (Ex: Replicate)
                # Simulação:
                res = "https://via.placeholder.com/600" 
                st.session_state[f"res_{key_prefix}"] = res
    
    # Exibir Resultado e Download
    if f"res_{key_prefix}" in st.session_state:
        st.markdown("### Resultado:")
        resultado = st.session_state[f"res_{key_prefix}"]
        if tipo == "Imagem": st.image(resultado)
        else: st.video(resultado)
        
        # Botão Baixar
        st.download_button(
            label="📥 BAIXAR RESULTADO",
            data=requests.get(resultado).content,
            file_name=f"projeto_{tipo}.{'png' if tipo=='Imagem' else 'mp4'}",
            key=f"dl_{key_prefix}",
            use_container_width=True
        )

with tab1: processar_geracao("Imagem", "img")
with tab2: processar_geracao("Vídeo", "vid")

# --- 3. LOTE ---
st.markdown("---")
if st.expander("📦 Ver Fila de Produção em Lote"):
    st.info("Aqui aparecerão seus projetos adicionados.")
