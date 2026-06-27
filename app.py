import streamlit as st
from huggingface_hub import InferenceClient

# Configuração da página para ficar limpa e vertical
st.set_page_config(page_title="Gerador Criativo AI", layout="centered")

st.title("Gerador de imagens com AI online: Crie imagens a partir de texto")

# Abas de navegação
tab1, tab2 = st.tabs(["🖼️ Gerar Imagem", "🎥 Gerar Vídeo"])

with tab1:
    prompt = st.text_input("Descreva o que deseja criar...")
    modelo = st.selectbox("Selecione a IA:", ["Stable Diffusion XL", "Outro Modelo Gratuito"])
    proporcao = st.radio("Proporção:", ["1:1", "9:16", "16:9"], horizontal=True)
    
    referencias = st.file_uploader("Upload de referências (até 5)", accept_multiple_files=True)
    
    if st.button("GERAR"):
        st.write("Gerando 3 opções para você...")
        # Aqui entra a lógica que conecta com o Hugging Face
        col1, col2, col3 = st.columns(3) # Apenas para exibir as 3 opções
        st.write("Escolha sua favorita abaixo:")

with tab2:
    st.write("Função de vídeo disponível após selecionar uma imagem.")

# Rodapé de Doação
st.markdown("---")
st.markdown("### Gostou do app? Ajude a manter o projeto gratuito!")
st.text("Insira aqui seu QR Code ou link do Pix")