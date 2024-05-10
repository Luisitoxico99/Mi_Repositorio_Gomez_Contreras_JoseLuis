import nltk
from nltk.tokenize import word_tokenize
from nltk.parse import RecursiveDescentParser

# Descargar los recursos necesarios de NLTK (solo es necesario la primera vez)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('treebank')

# Definir la oración de ejemplo
oracion = "El gato come pescado."

# Tokenizar la oración en palabras
palabras = word_tokenize(oracion)

# Realizar el etiquetado gramatical de las palabras
etiquetado = nltk.pos_tag(palabras)

# Crear un analizador sintáctico descendente recursivo
parser = RecursiveDescentParser(nltk.grammar.FeatureChartGrammar.fromstring('''
    S -> NP VP
    NP -> Det N
    VP -> V NP
    Det -> 'El'
    N -> 'gato' | 'pescado'
    V -> 'come'
'''))

# Realizar el análisis sintáctico de la oración
for arbol in parser.parse(palabras):
    print(arbol)
