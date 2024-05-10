import nltk
from nltk.corpus import brown

# Descargar el corpus Brown (si no está descargado previamente)
nltk.download('brown')

# Obtener las categorías de texto disponibles en el corpus Brown
categorias = brown.categories()

# Elegir una categoría de texto para entrenar el modelo de lenguaje (por ejemplo, noticias)
texto = brown.sents(categories='news')

# Dividir el corpus en datos de entrenamiento y datos de prueba
datos_entrenamiento = texto[:int(0.8 * len(texto))]
datos_prueba = texto[int(0.8 * len(texto)):]

# Entrenar un modelo de lenguaje de unigramas utilizando el corpus de entrenamiento
frecuencia_unigramas = nltk.FreqDist([palabra.lower() for oracion in datos_entrenamiento for palabra in oracion])
total_palabras = len([palabra for oracion in datos_entrenamiento for palabra in oracion])

# Calcular la probabilidad de unigramas
probabilidad_unigramas = {palabra: frecuencia_unigramas[palabra] / total_palabras for palabra in frecuencia_unigramas}

# Ejemplo de uso del modelo de lenguaje
palabra_ejemplo = 'the'
probabilidad_ejemplo = probabilidad_unigramas.get(palabra_ejemplo.lower(), 0)
print("Probabilidad de la palabra '{}': {}".format(palabra_ejemplo, probabilidad_ejemplo))
