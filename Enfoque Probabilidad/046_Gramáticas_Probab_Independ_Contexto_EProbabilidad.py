import nltk

# Definir una PCFG simple
pcfg = nltk.PCFG.fromstring("""
    S -> NP VP [1.0]
    NP -> Det N [0.6] | NP PP [0.4]
    VP -> V NP [0.7] | VP PP [0.3]
    PP -> P NP [1.0]
    Det -> 'the' [0.8] | 'a' [0.2]
    N -> 'cat' [0.5] | 'dog' [0.5]
    V -> 'chased' [0.7] | 'ate' [0.3]
    P -> 'in' [0.6] | 'on' [0.4]
""")

# Imprimir la PCFG
print(pcfg)

# Generar una oración aleatoria a partir de la PCFG
oracion_generada = pcfg.productions().pop().lhs().generate()
print("Oración generada:", ' '.join(oracion_generada))
