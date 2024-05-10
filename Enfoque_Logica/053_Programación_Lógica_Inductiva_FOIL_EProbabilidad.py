class Clausula:
    def __init__(self, antecedente, consecuente):
        self.antecedente = antecedente  # Antecedente de la cláusula (lista de características)
        self.consecuente = consecuente  # Consecuente de la cláusula (etiqueta)

def FOIL(ejemplos_positivos, ejemplos_negativos, caracteristicas):
    clausulas = []
    for ejemplo_positivo in ejemplos_positivos:
        for ejemplo_negativo in ejemplos_negativos:
            clausula_antecedente = []
            for caracteristica in caracteristicas:
                if ejemplo_positivo[caracteristica] != ejemplo_negativo[caracteristica]:
                    clausula_antecedente.append((caracteristica, ejemplo_positivo[caracteristica]))
            clausula_consecuente = ejemplo_positivo['etiqueta']
            clausulas.append(Clausula(clausula_antecedente, clausula_consecuente))
    return clausulas

# Ejemplo de uso
# Supongamos que tenemos un conjunto de datos con tres características: x1, x2 y x3
# Y queremos clasificar las instancias en dos clases: 0 o 1

# Definimos algunos ejemplos positivos y negativos
ejemplos_positivos = [
    {'x1': 1, 'x2': 0, 'x3': 1, 'etiqueta': 1},
    {'x1': 0, 'x2': 1, 'x3': 1, 'etiqueta': 1},
]
ejemplos_negativos = [
    {'x1': 0, 'x2': 0, 'x3': 0, 'etiqueta': 0},
    {'x1': 1, 'x2': 1, 'x3': 0, 'etiqueta': 0},
]

# Definimos las características
caracteristicas = ['x1', 'x2', 'x3']

# Aplicamos el algoritmo FOIL
clausulas = FOIL(ejemplos_positivos, ejemplos_negativos, caracteristicas)

# Imprimimos las cláusulas generadas
for clausula in clausulas:
    print("Si", clausula.antecedente, "entonces la etiqueta es", clausula.consecuente)
