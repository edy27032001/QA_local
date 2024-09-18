from flask import Flask, request, render_template
from transformers import AutoTokenizer, TFAutoModelForQuestionAnswering, pipeline
from werkzeug.utils import secure_filename
import os
from pdfminer.high_level import extract_text

app = Flask(__name__)

# Carga el modelo y el tokenizador
model_name = "./modelo_local"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = TFAutoModelForQuestionAnswering.from_pretrained(model_name)

# Si has guardado el modelo como .h5, carga los pesos
model.load_weights("./modelo_local/tf_model.h5")

# Crea el pipeline de QA
qa_pipeline = pipeline("question-answering", model=model, tokenizer=tokenizer)

# Ruta para almacenar archivos subidos
UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def home():
    context = ""

    if request.method == 'POST':
        # Verifica qué acción está solicitando el usuario
        action = request.form['action']
        question = request.form.get('question', '')
        context = request.form.get('context', '')

        # Si el usuario ha solicitado extraer el contenido del PDF
        if action == 'Extraer contenido del PDF':
            if 'pdf' in request.files:
                pdf_file = request.files['pdf']

                if pdf_file.filename != '':
                    # Guarda el archivo
                    filename = secure_filename(pdf_file.filename)
                    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                    pdf_file.save(file_path)

                    # Extrae el texto del PDF
                    context = extract_text(file_path)

            # Regresa el contenido extraído del PDF y permite hacer una pregunta después
            return render_template('index.html', context=context)

        # Si el usuario ha solicitado obtener la respuesta a la pregunta
        elif action == 'Obtener respuesta' and context.strip():
            # Obtén la respuesta usando el contexto
            result = qa_pipeline(question=question, context=context)
            return render_template('index.html', answer=result['answer'], score=result['score'], context=context)

    return render_template('index.html', context=context)

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)
