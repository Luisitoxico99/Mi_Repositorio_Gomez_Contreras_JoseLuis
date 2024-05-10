import nltk
from nltk.translate import IBMModel1  # Importar el modelo de traducción IBM1 de nltk

# Datos de entrenamiento: pares de frases en inglés y español
training_data = [
    ("the house", "la casa"),
    ("the cat", "el gato"),
    ("the dog", "el perro"),
    ("a book", "un libro"),
    ("the sun", "el sol"),
]

# Separar las frases en inglés y español
english_sentences, spanish_sentences = zip(*training_data)

# Tokenizar las frases (convertirlas en listas de palabras)
english_sentences_tokenized = [nltk.word_tokenize(sentence) for sentence in english_sentences]
spanish_sentences_tokenized = [nltk.word_tokenize(sentence) for sentence in spanish_sentences]

# Entrenar el modelo de traducción IBM1 con los pares de frases
ibm1_model = IBMModel1.estimate(english_sentences_tokenized, spanish_sentences_tokenized, max_iter=10)

# Frase de prueba en inglés
test_sentence = "the cat in the house".split()

# Traducir la frase de prueba al español utilizando el modelo entrenado
translation = ibm1_model.translate(test_sentence)

# Imprimir la traducción
print("English Sentence:", test_sentence)
print("Spanish Translation:", translation)
