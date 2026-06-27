import streamlit as st
from PIL import Image

# Configuração da página
st.set_page_config(page_title="Gerador Criativo AI", layout="centered")

st.title("Gerador de imagens com AI online")

# Abas principais
aba1, aba2 = st.tabs(["🖼️ Gerar Imagem", "🎥 Gerar Vídeo"])

with aba1:
    prompt = st.text_input("Descreva o que deseja criar:")
    
    # Lógica de lote
    col_ia, col_qtd = st.columns([2, 1])
    with col_ia:
        modelo = st.selectbox("Selecione a IA:", ["Stable Diffusion XL", "Flux"])
    with col_qtd:
        quantidade = st.number_input("Quantidade (Lote):", min_value=1, max_value=5, value=3)
    
    proporcao = st.radio("Proporção:", ["1:1", "9:16", "16:9"], horizontal=True)
    
    # Referências
    referencias = st.file_uploader("Upload de referências (até 5)", accept_multiple_files=True)
    if referencias:
        st.write("Referências carregadas:")
        cols_ref = st.columns(len(referencias) if len(referencias) <= 5 else 5)
        for i, file in enumerate(referencias):
            if i < 5:
                cols_ref[i].image(file, use_container_width=True)

    if st.button("GERAR LOTE"):
        st.write(f"Gerando {quantidade} imagens...")
        # Simulação da grade de resultados
        cols = st.columns(3)
        for i in range(quantidade):
            col_atual = cols[i % 3]
            with col_atual:
                st.image("https://via.placeholder.com/300", caption=f"Resultado {i+1}")
                st.download_button(f"Baixar {i+1}", data=b"dados", file_name=f"imagem_{i+1}.png")

with aba2:
    st.write("### Gerador de Vídeos")
    st.info("Selecione uma imagem gerada anteriormente para animar.")
    # Local para vídeo
    if st.button("GERAR VÍDEO"):
        st.write("Processando animação...")

# Rodapé de Doação
st.markdown("---")
st.markdown("### Gostou do app? Ajude a manter o projeto gratuito!")
st.write("Sua doação ajuda a manter o servidor no ar. [Insira seu link Pix aqui]")
