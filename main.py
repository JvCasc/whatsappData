import streamlit as st
from modulos import mensagens, txt_excel, ano_mes
import io

st.set_page_config(page_title="Wrapped", page_icon="🐢")

st.markdown("""
<style>
.stAppDeployButton { display: none; }
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

st.title("🐢 Whatsapp Wrapped")

# --------- Estado ---------
if "uploaded_file" not in st.session_state:
    st.session_state.uploaded_file = None
if "csv_pronto" not in st.session_state:
    st.session_state.csv_pronto = False
if "acao" not in st.session_state:
    st.session_state.acao = None         # qual botão foi clicado
if "resultado_botao1" not in st.session_state:
    st.session_state.resultado_botao1 = None  # (falador, nMensagens)
if "resultado_botao2" not in st.session_state:
    st.session_state.resultado_botao1 = None  # (periodo, nMensagensMes)

# --------- Funções (defina ANTES de usar) ---------
def processar_upload(uf):
    stringio = io.StringIO(uf.getvalue().decode("utf-8"))
    stringio.seek(0)
    txt_excel.txt_to_csv(stringio)
    st.session_state.csv_pronto = True

def executar_botao1():
    falador, n = mensagens.falador("whatsapp_conversa_tabela.csv")
    st.session_state.resultado_botao1 = (falador, n)
    st.session_state.acao = "botao1"

def executar_botao2():
    periodo, nMensagensMes = ano_mes.periodo_mes("whatsapp_conversa_tabela.csv")
    st.session_state.resultado_botao2 = (periodo, nMensagensMes)
    st.session_state.acao = "botao2"

# --------- Layout superior (botões em colunas) ---------
col1, col2, col3 = st.columns(3)

with col1:
    if st.button('👤 Enviou + mensagens', use_container_width=True):
        if st.session_state.csv_pronto:
            executar_botao1()
        else:
            st.warning("Por favor, envie o arquivo .txt antes.")

with col2:
    if st.button('⏰ Atividade do grupo', use_container_width=True):
        if st.session_state.csv_pronto:
            executar_botao2()
        else:
            st.warning("Envie o arquivo .txt para ver a atividade.")

with col3:
    if st.button('✏️ Palavra mais dita', use_container_width=True):
        if st.session_state.csv_pronto:
            st.session_state.acao = "palavra"
        else:
            st.warning("Envie o arquivo .txt para ver a palavra mais dita.")

# --------- Uploader (fica embaixo visualmente) ---------
uploader_placeholder = st.empty()
if st.session_state.uploaded_file is None:
    uf = uploader_placeholder.file_uploader(
        "Escolha o arquivo .txt exportado do WhatsApp",
        type="txt",
        accept_multiple_files=False,
        key="file_uploader_key"
    )
    if uf:
        st.session_state.uploaded_file = uf
        processar_upload(uf)
        uploader_placeholder.empty()
        st.success("Arquivo processado com sucesso! ✅")

# --------- RODAPÉ: área única de saída (fora das columns) ---------
rodape = st.container()
with rodape:
    if st.session_state.acao == "botao1" and st.session_state.resultado_botao1:
        falador, n = st.session_state.resultado_botao1
        st.subheader("👑 Resultado")
        st.text(f"Quem enviou mais mensagem: {falador} com {n} mensagens!")
        # Se quiser exibir imagem/gráfico aqui, ele não fica limitado pelas columns.
    elif st.session_state.acao == "botao2" and st.session_state.resultado_botao2:
        periodo, nMensagensMes = st.session_state.resultado_botao2 
        mes = periodo["AnoMes"] 
        nMMes = periodo["Mensagem"]
        st.subheader("⏰ Atividade do grupo")
        st.text(f"Mês mais ativo: {mes} com {nMMes} mensagens!")
    elif st.session_state.acao == "palavra":
        st.subheader("🔤 Palavra mais dita")
        st.info("…renderize nuvem de palavras/tabela aqui…")
