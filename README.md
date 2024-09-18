# QA_local
Este es un repositorio donde se encuentra el código usado para desplegar el modelo QA de forma local para responder a preguntas sobre el contenido extraído de tareas académicas de la UNL usando el framework FlaskProyecto de Question Answering basado en Flask

# Requisitos
Antes de comenzar, asegúrate de tener los siguientes componentes instalados:

Python 3.7 o superior
Pip para gestionar paquetes de Python

# Instalación
Clona el repositorio en tu máquina local:
Abre una cmd o crea una carpeta y abrela con un editor de código como lo es Visual Studio Code
## Copiar código
git clone https://github.com/tu-usuario/tu-repositorio.git
Ingresa al repositorio 
cd tu-repositorio

# Crea y activa un entorno virtual (opcional pero recomendado):
## Copiar código
python -m venv venv
source venv/bin/activate  # En Linux/MacOS
.\venv\Scripts\activate   # En Windows

# Instala las dependencias del proyecto:
## Copiar código
pip install -r requirements.txt
### Configuración del modelo
Ejecuta el script download_model.py(esto descargará todos los componentes del modelo y los ubicará en una carpeta nueva llamada modelo_local)
o 
Descarga el modelo TFDistilBertForQuestionAnswering preentrenado desde Hugging Face(edyfjm), asegúrate de tener la carpeta modelo_local en la raíz del proyecto.

# Uso
## Inicia la aplicación Flask:
### Copiar código
python app.py
Accede a la aplicación:
Abre tu navegador web y ve a:
http://127.0.0.1:5000
Ahora ya puedes usar el modelo de forma local usando una interfaz, esto permite al usuario:

Subir PDF o escribir un contexto manualmente(Puedes pegar el texto del contexto directamente o bien, puedes subir un archivo PDF para extraer el contexto automáticamente).
Ingresa tu pregunta y obtén la respuesta basada en el contexto proporcionado.
