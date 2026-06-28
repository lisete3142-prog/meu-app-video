import streamlit as st
import os

# --- CONFIGURAÇÃO DA SKIN (CSS PROFISSIONAL) ---
def local_css():
    st.markdown("""
    <style>
    /* Remover espaços padrão do Streamlit */
    .block-container { padding-top: 2rem; max-width: 800px; }
    
    /* Estilo dos Botões de Modo */
    div.stButton > button {
        width: 100%; height: 60px; font-size: 18px; border-radius: 12px;
        border: 2px solid #ddd; background-color: #f9f9f9; font-weight: bold;
    }
    div.stButton > button:hover { border-color: #007bff; color: #007bff; }
    
    /* Caixa de Prompt */
    .stTextArea textarea { border-radius: 15px; border: 2px solid #ccc; height: 120px; }
    
    /* Cards de Referência */
    .upload-box { border: 2px dashed #ccc; padding: 20px; border-radius: 15px; text-align: center; }
    
    /* Botões de Ação Final */
    .action-btn { background-color: #007bff; color: white; border-radius: 8px; }
    </style>
    """, unsafe_allow_html=True)

local_css()

# --- TELA PRINCIPAL ---
st.title("🎨 Gerador Criativo AI")
st.markdown("Crie projetos a partir de texto com qualidade profissional.")

# Seletor de Modo (Abas)
tab1, tab2 = st.tabs(["🖼️ Gerar Imagem", "🎥 Gerar Vídeo"])

# --- LÓGICA DE GERAÇÃO ---
def render_gerador(tipo):
    st.subheader(f"Configurações de {tipo}")
    
    # Modelo
    modelo = st.selectbox(f"Escolha o Modelo de {tipo}", ["Flux 1.1 Pro", "Stable Diffusion XL", "DALL-E 3"])
    
    # Prompt
    prompt = st.text_area("Descreva seu projeto:", placeholder="Ex: Uma paisagem futurista...")
    
    # Referências
    st.markdown("### Referências (Até 5)")
    uploaded_files = st.file_uploader("Arraste até 5 imagens aqui", accept_multiple_files=True, type=['png', 'jpg', 'jpeg'])
    
    # Proporção
    st.markdown("### Proporção")
    proporcao = st.radio("Escolha o formato:", ["1:1 (Instagram)", "9:16 (TikTok)", "16:9 (YouTube)"], horizontal=True)
    
    # Botão Gerar
    if st.button(f"🚀 GERAR {tipo.upper()}", use_container_width=True):
        if not prompt:
            st.error("Escreva um prompt para começar!")
        else:
            st.success(f"Gerando {tipo} com {modelo}...")
            # Aqui entrará a integração com API (Replicate)

    # Botão Lote
    if st.button("➕ Adicionar à Fila de Lote"):
        st.info("Adicionado à fila de produção!")

# --- EXECUÇÃO DOS MODOS ---
with tab1:
    render_gerador("Imagem")

with tab2:
    render_gerador("Vídeo")

# --- PAINEL DE LOTE (OCULTO/DISCRETO) ---
with st.expander("📦 Fila de Produção em Lote"):
    st.write("Histórico de produção em massa...")
    if st.button("📥 Baixar Tudo (ZIP)"):
        st.write("Preparando download...")
