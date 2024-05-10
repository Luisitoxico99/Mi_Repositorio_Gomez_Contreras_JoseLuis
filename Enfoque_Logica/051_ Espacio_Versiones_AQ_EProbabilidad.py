class Regla:
    def __init__(self, caracteristica, valor, etiqueta):
        self.caracteristica = caracteristica  # Característica utilizada en la regla
        self.valor = valor  # Valor de la característica
        self.etiqueta = etiqueta  # Etiqueta asignada por la regla

def generar_regla(ejemplos_positivos, ejemplos_negativos, caracteristicas):
    reglas = []
    for caracteristica in caracteristicas:
        # Regla para ejemplos positivos
        positivos_para_caracteristica = [ejemplo for ejemplo in ejemplos_positivos if ejemplo[caracteristica] == 1]
        if len(positivos_para_caracteristica) == len(ejemplos_positivos):
            reglas.append(Regla(caracteristica, 1, 1))
        # Regla para ejemplos negativos
        negativos_para_caracteristica = [ejemplo for ejemplo in ejemplos_negativos if ejemplo[caracteristica] == 0]
        if len(negativos_para_caracteristica) == len(ejemplos_negativos):
            reglas.append(Regla(caracteristica, 0, 0))
    return reglas

# Ejemplo de uso
# Supongamos que tenemos un conjunto de datos con dos características: x1 y x2
# Y queremos clasificar las instancias en dos clases: 0 o 1

# Definimos algunos ejemplos positivos y negativos
ejemplos_positivos = [
    {0: 1, 1: 1},
    {0: 1, 1: 0},
    {0: 1, 1: 1},
]
ejemplos_negativos = [
    {0: 0, 1: 0},
    {0: 0, 1: 1},
    {0: 0, 1: 0},
]

# Definimos las características
caracteristicas = [0, 1]

# Generamos la regla
reglas = generar_regla(ejemplos_positivos, ejemplos_negativos, caracteristicas)

# Imprimimos las reglas generadas
for regla in reglas:
    print("Si", "Caracteristica", regla.caracteristica, "es igual a", regla.valor, "entonces la etiqueta es", regla.etiqueta)
