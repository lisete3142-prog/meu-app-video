import streamlit as st
import zipfile
import os

# --- CSS MODERNO ---
def aplicar_css():
    st.markdown("""
    <style>
    .block-container { padding-top: 2rem; max-width: 900px; }
    h1 { font-size: 2.5rem; color: #222; text-align: center; }
    h2, h3 { color: #333; }
    
    /* Botões principais */
    div.stButton > button {
        width: 100%; height: 55px; font-size: 18px; border-radius: 12px;
        border: none; background: linear-gradient(90deg,#007bff,#00c6ff);
        color: white; font-weight: bold;
    }
    div.stButton > button:hover { opacity: 0.9; }
    
    /* Área de texto */
    .stTextArea textarea {
        border-radius: 12px; border: 2px solid #ccc; padding: 12px;
        font-size: 16px;
    }
    
    /* Upload */
    .stFileUploader {
        border: 2px dashed #aaa; border-radius: 12px; padding: 20px;
        background-color: #f9f9f9;
    }
    
    /* Expander */
    .streamlit-expanderHeader { font-weight: bold; color: #007bff; }
    </style>
    """, unsafe_allow_html=True)

aplicar_css()

# --- TÍTULO ---
st.title("🎨 Gerador Criativo AI")
st.markdown("Crie imagens e vídeos a partir de texto com referências visuais para manter consistência.")

# --- ABAS ---
tab1, tab2 = st.tabs(["🖼️ Gerar Imagem", "🎥 Gerar Vídeo"])

# --- FUNÇÃO DE GERAÇÃO ---
def render_gerador(tipo):
    st.subheader(f"Configurações de {tipo}")
    
    # Seleção de modelo (nomes genéricos e amigáveis)
    modelo = st.selectbox(f"Escolha o modelo de {tipo}", 
                          ["Modelo Gratuito", "Modelo Avançado", "Modelo Premium"])
    
    # Prompt
    prompt = st.text_area("✍️ Descreva seu projeto:", 
                          placeholder="Ex: Uma personagem futurista em diferentes cenários...")
    
    # Upload de referências
    st.markdown("### 📎 Referências (mínimo 2 para consistência)")
    arquivos = st.file_uploader("Arraste até 5 imagens aqui", 
                                accept_multiple_files=True, type=['png','jpg','jpeg'])
    
    # Proporção
    proporcao = st.radio("📐 Escolha o formato:", 
                         ["1:1 (Quadrado)", "9:16 (Vertical)", "16:9 (Horizontal)"], horizontal=True)
    
    # Botão de geração
    if st.button(f"🚀 GERAR {tipo.upper()}", use_container_width=True):
        if not prompt:
            st.error("Digite um prompt para começar!")
        elif len(arquivos) < 2:
            st.error("Envie pelo menos 2 imagens de referência para manter consistência dos personagens!")
        else:
            st.success(f"Gerando {tipo} com {modelo} no formato {proporcao}...")
            # Aqui entraria a integração real com API de IA
            st.image("exemplo.png", caption="Pré-visualização do resultado")  # Exemplo
            with open("exemplo.png", "rb") as file:
                st.download_button("📥 Baixar Resultado", file, file_name="resultado.png", mime="image/png")
    
    # Botão de lote
    if st.button("➕ Adicionar à Fila de Lote"):
        if len(arquivos) < 2:
            st.error("Para produção em lote, é obrigatório enviar pelo menos 2 referências!")
        else:
            st.info("Projeto adicionado à fila de produção!")

# --- EXECUÇÃO ---
with tab1:
    render_gerador("Imagem")
with tab2:
    render_gerador("Vídeo")

# --- PAINEL DE LOTE ---
with st.expander("📦 Fila de Produção em Lote"):
    st.write("Aqui aparecerá o histórico dos projetos adicionados.")
    if st.button("📥 Baixar Tudo (ZIP)"):
        # Exemplo de criação de ZIP
        with zipfile.ZipFile("resultados.zip", "w") as zipf:
            zipf.write("exemplo.png")
        with open("resultados.zip", "rb") as file:
            st.download_button("📥 Baixar ZIP", file, file_name="resultados.zip", mime="application/zip")
