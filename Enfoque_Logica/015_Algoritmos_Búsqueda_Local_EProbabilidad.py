import random
import math

def objetivo(x):
    return -x**2 + 5*x + 10  # Función objetivo (maximizar)

def hill_climbing(solucion_inicial, paso, num_iteraciones):
    solucion_actual = solucion_inicial
    for _ in range(num_iteraciones):
        vecino = solucion_actual + random.uniform(-paso, paso)
        if objetivo(vecino) > objetivo(solucion_actual):
            solucion_actual = vecino
    return solucion_actual

def simulated_annealing(solucion_inicial, paso, temperatura_inicial, enfriamiento, num_iteraciones):
    solucion_actual = solucion_inicial
    temperatura = temperatura_inicial
    for _ in range(num_iteraciones):
        vecino = solucion_actual + random.uniform(-paso, paso)
        diferencia_objetivo = objetivo(vecino) - objetivo(solucion_actual)
        if diferencia_objetivo > 0 or random.random() < math.exp(diferencia_objetivo / temperatura):
            solucion_actual = vecino
        temperatura *= enfriamiento
    return solucion_actual

# Ejemplo de uso
solucion_inicial = 0
paso = 0.1
num_iteraciones = 1000

solucion_hill_climbing = hill_climbing(solucion_inicial, paso, num_iteraciones)
print("Solución encontrada por Hill Climbing:", solucion_hill_climbing, "Valor de la función objetivo:", objetivo(solucion_hill_climbing))

temperatura_inicial = 100.0
enfriamiento = 0.95

solucion_simulated_annealing = simulated_annealing(solucion_inicial, paso, temperatura_inicial, enfriamiento, num_iteraciones)
print("Solución encontrada por Simulated Annealing:", solucion_simulated_annealing, "Valor de la función objetivo:", objetivo(solucion_simulated_annealing))
