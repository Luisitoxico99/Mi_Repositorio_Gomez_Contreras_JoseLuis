import nltk

# Definir una PLFG simple
plfg = nltk.PCFG.fromstring("""
    S    -> NP VP      [1.0]
    NP   -> Det N      [0.6] | NP PP [0.4]
    VP   -> V NP      [0.7] | VP PP [0.3]
    PP   -> P NP      [1.0]
    Det  -> 'the'     [0.8] | 'a' [0.2]
    N    -> 'cat'     [0.5] | 'dog' [0.5]
    V    -> 'chased'  [0.7] | 'ate' [0.3]
    P    -> 'in'      [0.6] | 'on' [0.4]
""")

# Imprimir la PLFG
print(plfg)

# Generar un árbol de derivación aleatorio a partir de la PLFG
arbol_derivacion = plfg.productions().pop().lhs().produce()
print("Árbol de derivación:", arbol_derivacion)
