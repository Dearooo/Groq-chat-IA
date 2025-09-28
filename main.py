import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client = OpenAI(api_key=GROQ_API_KEY, base_url="https://api.groq.com/openai/v1")

# Configuração da página
st.set_page_config(page_title="Malu 🌸", page_icon="🌸", layout="wide")

# Inicializa estado para armazenar mensagens
if "messages" not in st.session_state:
    st.session_state.messages = []

# Função para enviar mensagem
def enviar_mensagem():
    if st.session_state.input_text:
        st.session_state.messages.append({"role": "user", "content": st.session_state.input_text})
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
             messages=[
                {"role": "user", "content": st.session_state.input_text},
                {"role": "system", "content": "Carinhosa, me trata como amiga Afeminada, Organizada, separa quase todos os assuntos em tópicos, Tem clareza e é bem direta, Incentivadora, tudo que eu faço ela manda mensagem de carinho e motivação"}
            ]
        )
        st.session_state.messages.append({"role": "Malu 🌸", "content": response.choices[0].message.content})
        st.session_state.input_text = ""

# Layout principal
col1, col2 = st.columns([1, 3], gap="small")

# Coluna da imagem
with col1:
    st.image("animacao_gif.gif")

# Coluna do chat
with col2:
    # Área de mensagens com scroll
    chat_html = '<div style="height:400px; overflow-y:auto; padding:10px; border:1px solid #444; border-radius:10px; background-color:#111;">'
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            chat_html += f'<div style="text-align:right; margin-bottom:5px;"><span style="background-color:#0f62fe; padding:5px 10px; border-radius:10px; color:white;">{msg["content"]}</span></div>'
        else:
            chat_html += f'<div style="text-align:left; margin-bottom:5px;"><div style="background-color:#333; padding:5px 10px; border-radius:10px; color:white;">Malu 🌸: {msg["content"]}</div></div>'
    chat_html += """</div>
    <script>
    var chatbox = document.getElementById('chatbox');
    chatbox.scrollTop = chatbox.scrollHeight;
    </script>"""
    st.markdown(chat_html, unsafe_allow_html=True)

    # Caixa de input fixa
    st.text_input("Fale com a Malu...", key="input_text", on_change=enviar_mensagem)
