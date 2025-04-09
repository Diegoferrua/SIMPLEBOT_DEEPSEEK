# SimpleBot con ChatGPT-4

SimpleBot es un chatbot inteligente diseñado para ofrecer productos siguiendo reglas específicas de interacción, como asegurar un trato amable y gestionar servicios como brindar informacion util segun el tipo de envio Utilizando la potente tecnología de ChatGPT-4 de OpenAI, SimpleBot puede comprender y procesar solicitudes complejas, proporcionando respuestas y recomendaciones personalizadas a los usuarios.

## Descripción

Este proyecto implementa una arquitectura básica que permite crear un chatbot personalizado con capacidades avanzadas de comprensión y generación de texto. A través de un conjunto de reglas predefinidas, SimpleBot puede ofrecer productos y servicios de manera eficiente y amigable, asegurando una experiencia de usuario óptima. Desarrollado en Python y utilizando la biblioteca principal de OpenAI, este bot es capaz de manejar conversaciones complejas, entender las necesidades del usuario, y actuar de acuerdo con las políticas de servicio establecidas, como el cobro de delivery y el mantenimiento de un trato respetuoso en todo momento.

## Características

- **Interacción Natural**: Utiliza ChatGPT-4 para generar respuestas naturales y coherentes.
- **Reglas Personalizadas**: Implementa reglas específicas para la oferta de productos y servicios.
- **Identificación de forma de envió y pago**: Capacidad para gestionar solicitudes de acuerdo al tipo de envió y pago
- **Fácil de Configurar**: Desarrollado en Python con una configuración simple y documentación clara.

## Requisitos Previos

Antes de comenzar, asegúrate de tener lo siguiente:

- Python 3.8 o superior
- Acceso a la API de OpenAI (necesitarás una clave API de OpenAI)

## Configuración

Para configurar SimpleBot en tu entorno local, sigue estos pasos:

1. **Clonar el Repositorio**

```bash
git clone https://github.com/macespinoza/simplebot-chatgpt4.git
cd simplebot-chatgpt4
```
2. **Configurar las Claves de API**
edita el archivo clave_api.txt e ingresa tu propia clave api
```bash
with open("clave_api.txt") as archivo:
	openai.api_key = archivo.readline()
```
3. **Uso Consola**
```bash
python chatbot_gen.py
```
Sigue las instrucciones en pantalla para chatear con SimpleBot y explorar sus funcionalidades

3.1. **Uso Streamlit**
```bash
streamlit run main_str.py
```
Sigue las instrucciones en pantalla para chatear con SimpleBot y explorar sus funcionalidades.

## Contribuir

¡Las contribuciones son bienvenidas! Si deseas contribuir al proyecto, por favor:

1.  Haz fork del repositorio.
2.  Crea una nueva rama para tus características o correcciones.
3.  Envía un pull request con tus cambios.

## Contacto

Para cualquier consulta o colaboración, por favor, no dudes en contactar al autor del proyecto.
