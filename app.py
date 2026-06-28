
def render_gerador(tipo, prefixo):
    st.subheader(f"Configurações de {tipo}")
    
    # Modelo
    modelo = st.selectbox(f"Escolha o modelo de {tipo}", 
                          ["Modelo Gratuito", "Modelo Avançado", "Modelo Premium"],
                          key=f"modelo_{prefixo}")
    
    # Prompt
    prompt = st.text_area("✍️ Descreva seu projeto:", 
                          placeholder="Ex: Uma personagem futurista em diferentes cenários...",
                          key=f"prompt_{prefixo}")
    
    # Upload de referências
    st.markdown("### 📎 Referências (mínimo 2 para consistência)")
    arquivos = st.file_uploader("Arraste até 5 imagens aqui", 
                                accept_multiple_files=True, type=['png','jpg','jpeg'],
                                key=f"upload_{prefixo}")
    
    # Proporção
    proporcao = st.radio("📐 Escolha o formato:", 
                         ["1:1 (Quadrado)", "9:16 (Vertical)", "16:9 (Horizontal)"], 
                         horizontal=True, key=f"proporcao_{prefixo}")
    
    # Botão de geração
    if st.button(f"🚀 GERAR {tipo.upper()}", use_container_width=True, key=f"gerar_{prefixo}"):
        if not prompt:
            st.error("Digite um prompt para começar!")
        elif len(arquivos) < 2:
            st.error("Envie pelo menos 2 imagens de referência para manter consistência dos personagens!")
        else:
            st.success(f"Gerando {tipo} com {modelo} no formato {proporcao}...")
            st.image("exemplo.png", caption="Pré-visualização do resultado")
            with open("exemplo.png", "rb") as file:
                st.download_button("📥 Baixar Resultado", file, file_name="resultado.png", mime="image/png", key=f"download_{prefixo}")
    
    # Botão de lote
    if st.button("➕ Adicionar à Fila de Lote", key=f"lote_{prefixo}"):
        if len(arquivos) < 2:
            st.error("Para produção em lote, é obrigatório enviar pelo menos 2 referências!")
        else:
            st.info("Projeto adicionado à fila de produção!")
