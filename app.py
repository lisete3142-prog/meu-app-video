import streamlit as st

# Configuração da página
st.set_page_config(page_title="Gerador Criativo AI", layout="centered")

# Título
st.title("Gerador de imagens com AI online: Crie imagens a partir de texto")

# Abas
aba1, aba2 = st.tabs(["🖼️ Gerar Imagem", "🎥 Gerar Vídeo"])

with aba1:
    st.text_input("Descreva o que deseja criar...")
    st.selectbox("Selecione a IA:", ["Stable Diffusion XL"])
    st.write("Proporção:")
    st.radio("", ["1:1", "9:16", "16:9"], horizontal=True)
    st.write("Upload de referências (até 5)")
    st.file_uploader("", accept_multiple_files=True)
    st.button("GERAR")

with aba2:
    st.write("Configurações de vídeo...")

# Rodapé
st.markdown("---")
