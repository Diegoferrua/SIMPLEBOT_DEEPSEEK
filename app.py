import streamlit as st
from chatbot_gen import enviar_mensajes, contexto

st.set_page_config(page_title="Chatbot GenAI", layout="centered")

st.title("Chatbot GenAI")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Escribe tu mensaje:", key="user_input")

if st.button("Enviar") and user_input:
    # Agrega el mensaje del usuario al contexto
    contexto.append({'role': 'user', 'content': user_input})
    # Obtiene la respuesta del bot
    respuesta = enviar_mensajes(contexto, temperature=0.7)
    contexto.append({'role': 'assistant', 'content': respuesta})
    # Guarda en el historial
    st.session_state.chat_history.append(("Tú", user_input))
    st.session_state.chat_history.append(("Bot", respuesta))

st.write("### Conversación")
for autor, mensaje in st.session_state.chat_history:
    st.markdown(f"**{autor}:** {mensaje}")

st.write("---")
st.write("Escribe tu mensaje y presiona 'Enviar' para conversar con el bot.")