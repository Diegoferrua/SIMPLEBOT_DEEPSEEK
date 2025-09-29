#requisitos Interfase Anaconda libreria OPENAI #licencia activa para el API OPENAI

import os
import openai
import sys
import requests
from dotenv import load_dotenv  # <-- nuevo import

# Cargar variables de entorno desde .env
load_dotenv()

# Obtener la clave desde la variable de entorno
api_key = os.getenv("DEEPSEEK_API_KEY")
openai.api_key = api_key
os.environ["OPENAI_API_KEY"] = api_key
    
with open("icenter.csv", encoding="utf-8") as archivo:
    producto_csv = archivo.read()

with open("reglas.txt", encoding="utf-8") as archivo:
    reglas = archivo.read()
    
#Creamos la memoria temporal
contexto = []
#registramos las reglas y productos
contexto.append({'role':'system', 'content':f"""{reglas} {producto_csv}"""})

#enviamos mensaje al modelo usando DeepSeek API
def enviar_mensajes(messages, model="deepseek-chat", temperature=0):
    url = "https://api.deepseek.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": model,
        "messages": messages,
        "temperature": temperature
    }
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]

#leemos el mensaje + agregamos al contexto | enviamos el contexto | + agregar respuesta al contexto
def recargar_mensajes(charla):
    contexto.append({'role':'user', 'content':f"{charla}"})
    response = enviar_mensajes(contexto,temperature=0.7)
    contexto.append({'role':'assistant','content':f"{response}"})
    print()
    print(response)
    
def main():
        while True:
            print()
            mensaje = input("Por favor, ingresa un mensaje (o 'exit' para salir)")
            
            if mensaje.lower() =='exit':
                break
            
            recargar_mensajes(mensaje)
            
if __name__=='__main__':
    main()

