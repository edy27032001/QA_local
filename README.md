# QA_local

Este es un repositorio donde se encuentra el código usado para desplegar un modelo de Question Answering (QA) de forma local para responder a preguntas sobre el contenido extraído de tareas académicas de la Universidad Nacional de Loja (UNL), utilizando el framework Flask.

## Requisitos

Antes de comenzar, asegúrate de tener los siguientes componentes instalados:

- **Python 3.7** o superior.
- **Pip** para gestionar paquetes de Python.

## Instalación

Clona el repositorio en tu máquina local:

1. Abre una terminal o crea una carpeta y ábrela con un editor de código, como Visual Studio Code.

2. Copia el siguiente código para clonar el repositorio:

    ```bash
    git clone https://github.com/edy27032001/QA_local.git
    ```

3. Ingresa al directorio del repositorio clonado:

    ```bash
    cd QA_local
    ```

## Creación y activación de un entorno virtual (opcional pero recomendado)

1. Crea un entorno virtual:

    ```bash
    python -m venv venv
    ```

2. Activa el entorno virtual:

    - En Linux/MacOS:

        ```bash
        source venv/bin/activate
        ```

    - En Windows:

        ```bash
        .\venv\Scripts\activate
        ```

## Instalación de dependencias

Instala todas las dependencias del proyecto que están listadas en el archivo `requirements.txt`:

```bash
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
