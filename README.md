# Chatbot GenAI con DeepSeek y Streamlit

Este proyecto es un chatbot que utiliza la API de DeepSeek y una interfaz web sencilla con Streamlit.

## Requisitos

- Python 3.8+
- Una clave válida de DeepSeek API

## Instalación

1. Clona el repositorio.
2. (Opcional pero recomendado) Crea y activa un entorno virtual:

   **Con venv:**
   ```bash
   python -m venv env_genai
   # En Windows:
   env_genai\Scripts\activate
   # En Linux/Mac:
   source env_genai/bin/activate
   ```

   **Con conda:**
   ```bash
   conda create -n env_genai python=3.11
   conda activate env_genai
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Crea el archivo `.env` en la raíz del proyecto con tu clave DeepSeek:

   ```bash
   DEEPSEEK_API_KEY=tu_clave_deepseek_aqui
   ```

5. Coloca tus archivos `icenter.csv` y `reglas.txt` en la raíz del proyecto.

## Uso

1. Ejecuta la aplicación web:

   ```bash
   streamlit run app.py
   ```

2. Abre el navegador en la URL que muestra Streamlit (por defecto http://localhost:8501).
3. Escribe tus mensajes en el chat y conversa con el bot.

## Estructura de archivos

- `app.py`: Interfaz web con Streamlit.
- `chatbot_gen.py`: Lógica del chatbot y conexión con DeepSeek.
- `.env`: Clave privada de DeepSeek (no compartir).
- `requirements.txt`: Dependencias del proyecto.
- `icenter.csv`: Productos o datos para el bot.
- `reglas.txt`: Reglas o instrucciones para el bot.

## Notas

- No subas tu archivo `.env` a repositorios públicos.
- Si tienes problemas con la codificación de archivos, asegúrate de que estén en UTF-8.
## Contribuir

¡Las contribuciones son bienvenidas! Si deseas contribuir al proyecto, por favor:

1.  Haz fork del repositorio.
2.  Crea una nueva rama para tus características o correcciones.
3.  Envía un pull request con tus cambios.

## Contacto

Para cualquier consulta o colaboración, por favor, no dudes en contactar al autor del proyecto.
