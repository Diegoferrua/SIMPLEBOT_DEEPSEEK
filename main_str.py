import os
from dotenv import load_dotenv
import openai
import streamlit as st

# Cargar variables de entorno
load_dotenv()
openai.api_key = os.getenv("DEEPSEEK_API_KEY")

with open("productos_textil.csv") as archivo:
    producto_csv = archivo.read()

with open("reglas.txt") as archivo:
    reglas = archivo.read()

# Inicializar contexto en sesión de Streamlit
if "contexto" not in st.session_state:
    st.session_state.contexto = [
        {'role': 'system', 'content': f"{reglas} {producto_csv}"}
    ]

# Función para enviar mensajes al modelo
def enviar_mensajes(messages, model="gpt-4", temperature=0.7):
    response = openai.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message.content

# Aplicación Streamlit
st.title("Demo de Chat - TextilProd🧵👕")

st.write("Bienvenido a TextilProd ")

mensaje = st.text_input("Escribe tu mensaje aquí:")

if st.button("Enviar"):
    if mensaje:
        st.session_state.contexto.append({'role': 'user', 'content': mensaje})
        respuesta = enviar_mensajes(st.session_state.contexto)
        st.session_state.contexto.append({'role': 'assistant', 'content': respuesta})
        st.success(respuesta)
    else:
        st.warning("Por favor escribe un mensaje antes de enviar.")

# Mostrar historial de conversación
st.subheader("Historial de conversación:")
for chat in st.session_state.contexto[1:]:  # Omitimos el primer system prompt
    if chat['role'] == 'user':
        st.markdown(f"**Usuario:** {chat['content']}")
    elif chat['role'] == 'assistant':
        st.markdown(f"**Asistente:** {chat['content']}")
