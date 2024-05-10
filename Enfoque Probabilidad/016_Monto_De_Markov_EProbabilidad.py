import numpy as np

# Definir la matriz de transición
# En este ejemplo, tenemos 3 estados: A, B y C
# La matriz de transición representa las probabilidades de pasar de un estado a otro
# Cada fila representa el estado actual y cada columna representa el próximo estado
# Por ejemplo, la entrada (i, j) representa la probabilidad de pasar del estado i al estado j
matriz_transicion = np.array([
    [0.7, 0.2, 0.1],  # Probabilidades de transición desde el estado A
    [0.3, 0.4, 0.3],  # Probabilidades de transición desde el estado B
    [0.5, 0.1, 0.4]   # Probabilidades de transición desde el estado C
])

# Definir el estado inicial
# En este ejemplo, comenzamos en el estado A con una probabilidad del 100%
estado_actual = 0  # Esto representa el estado A

# Generar una secuencia de estados basada en la matriz de transición
secuencia_estados = [estado_actual]
num_pasos = 10  # Número de pasos en la cadena de Markov

for _ in range(num_pasos):
    # Elegir el próximo estado basado en la matriz de transición y el estado actual
    proximo_estado = np.random.choice(range(len(matriz_transicion)), p=matriz_transicion[estado_actual])
    secuencia_estados.append(proximo_estado)
    estado_actual = proximo_estado

# Imprimir la secuencia de estados generada
print("Secuencia de estados generada:", secuencia_estados)
