
import streamlit as st
import requests

def render_gerador(tipo, key_prefix):
    st.subheader(f"Configurações de {tipo}")
    
    # 1. Referências Visualizadas
    uploaded_files = st.file_uploader(f"Carregar até 5 referências", accept_multiple_files=True, key=f"up_{key_prefix}")
    if uploaded_files:
        cols = st.columns(5)
        for i, file in enumerate(uploaded_files[:5]):
            with cols[i]:
                st.image(file, use_container_width=True)
    
    # 2. Prompt
    prompt = st.text_area("Descreva seu projeto:", key=f"prompt_{key_prefix}")
    
    # 3. Botão de Geração
    if st.button(f"🚀 GERAR {tipo.upper()}", key=f"btn_{key_prefix}"):
        with st.spinner("Gerando sua criação..."):
            # Aqui entra a chamada da sua API (Ex: Replicate)
            # Vamos simular que o 'resultado' é a URL do arquivo
            resultado_url = "https://example.com/imagem.png" 
            
            # Guardamos o resultado na sessão para o botão de download encontrar
            st.session_state[f"resultado_{key_prefix}"] = resultado_url
            
    # 4. EXIBIÇÃO DO RESULTADO E BOTÃO DE DOWNLOAD
    if f"resultado_{key_prefix}" in st.session_state:
        res = st.session_state[f"resultado_{key_prefix}"]
        
        st.markdown("### Resultado:")
        if tipo == "Imagem":
            st.image(res)
        else:
            st.video(res)
            
        # --- O BOTÃO DE DOWNLOAD ---
        # Baixamos o conteúdo da URL para o navegador
        try:
            conteudo = requests.get(res).content
            st.download_button(
                label="📥 BAIXAR RESULTADO",
                data=conteudo,
                file_name=f"projeto_{tipo}.{'png' if tipo == 'Imagem' else 'mp4'}",
                mime="image/png" if tipo == "Imagem" else "video/mp4",
                key=f"dl_{key_prefix}",
                use_container_width=True
            )
        except:
            st.error("Erro ao preparar o download.")

# Estrutura das abas
tab1, tab2 = st.tabs(["🖼️ Gerar Imagem", "🎥 Gerar Vídeo"])
with tab1: render_gerador("Imagem", "img")
with tab2: render_gerador("Vídeo", "vid")
