# Definimos un diccionario que contiene las probabilidades conjuntas P(A, B)
probabilidades_conjuntas = {
    ('A', 'B'): 0.3,
    ('A', '¬B'): 0.2,
    ('¬A', 'B'): 0.1,
    ('¬A', '¬B'): 0.4
}

# Definimos las probabilidades marginales P(A) y P(B)
probabilidad_A = sum(probabilidades_conjuntas[clave] for clave in probabilidades_conjuntas if clave[0] == 'A')
probabilidad_B = sum(probabilidades_conjuntas[clave] for clave in probabilidades_conjuntas if clave[1] == 'B')

# Definimos la variable condicional B dado A, P(B|A), y la normalizamos
probabilidad_B_dado_A = {clave[1]: probabilidades_conjuntas[clave] / probabilidad_A for clave in probabilidades_conjuntas if clave[0] == 'A'}

# Imprimimos los resultados
print("Probabilidad marginal de A:", probabilidad_A)
print("Probabilidad marginal de B:", probabilidad_B)
print("Probabilidad condicionada de B dado A:")
for evento, probabilidad in probabilidad_B_dado_A.items():
    print("P(B={}|A) = {:.2f}".format(evento, probabilidad))
