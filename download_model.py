from transformers import TFAutoModelForQuestionAnswering, AutoTokenizer

model_name = "edyfjm07/distilbert-base-uncased-QA1-finetuned-squad-es"

# Descarga el modelo y el tokenizador
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = TFAutoModelForQuestionAnswering.from_pretrained(model_name)

# Guarda el modelo y el tokenizador localmente
model.save_pretrained("./modelo_local")
tokenizer.save_pretrained("./modelo_local")

# Guarda el modelo en formato .h5
model.save_weights("./modelo_local/tf_model.h5")

print("Modelo descargado y guardado en formato .h5")
