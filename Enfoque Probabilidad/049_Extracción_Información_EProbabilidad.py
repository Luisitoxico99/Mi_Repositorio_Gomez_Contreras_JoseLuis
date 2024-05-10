import spacy

# Cargar el modelo de lenguaje en español de spaCy
nlp = spacy.load("es_core_news_sm")

# Definir un texto de ejemplo
texto = "El presidente de Estados Unidos, Joe Biden, se reunió con la canciller alemana Angela Merkel en Washington D.C."

# Procesar el texto con spaCy
doc = nlp(texto)

# Iterar sobre las entidades nombradas encontradas en el texto
for entidad in doc.ents:
    print(entidad.text, entidad.label_)
