import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import LidstoneProbDist
from nltk.util import ngrams
from collections import defaultdict

# Texto de ejemplo
texto = "El gato está en el tejado."

# Tokenización del texto en palabras
palabras = word_tokenize(texto.lower())

# Crear un modelo de lenguaje de trigramas
n = 3  # longitud del n-grama
trigramas = ngrams(palabras, n)

# Contar la frecuencia de cada n-grama
frecuencia_ngramas = defaultdict(int)
for trigrama in trigramas:
    frecuencia_ngramas[trigrama] += 1

# Función para predecir la siguiente palabra dada una secuencia de palabras
def predecir_siguiente_palabra(frase):
    frase_tokens = word_tokenize(frase.lower())
    ultimos_n_tokens = frase_tokens[-(n-1):]
    candidatos = defaultdict(float)
    
    # Calcular la probabilidad de cada palabra candidata
    for trigram, frecuencia in frecuencia_ngramas.items():
        if trigram[:n-1] == tuple(ultimos_n_tokens):
            candidatos[trigram[-1]] += frecuencia
    
    # Normalizar las probabilidades
    total_ocurrencias = sum(candidatos.values())
    for palabra, frecuencia in candidatos.items():
        candidatos[palabra] = frecuencia / total_ocurrencias
    
    # Devolver la palabra con la probabilidad más alta
    palabra_siguiente = max(candidatos, key=candidatos.get)
    return palabra_siguiente

# Ejemplo de uso
frase = "el gato está"
palabra_siguiente = predecir_siguiente_palabra(frase)
print("La siguiente palabra más probable después de '{}' es '{}'".format(frase, palabra_siguiente))
