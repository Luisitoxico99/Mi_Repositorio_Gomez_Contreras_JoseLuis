import numpy as np

# Función de transición de estado (modelo de movimiento)
def transicion_estado(x_t_1):
    # Aquí se define el modelo de movimiento del sistema
    # En este ejemplo, se asume un movimiento aleatorio
    return x_t_1 + np.random.normal(loc=0, scale=0.1, size=x_t_1.shape)

# Función de observación (modelo de medición)
def observacion_modelo(x_t):
    # Aquí se define el modelo de observación del sistema
    # En este ejemplo, se asume una observación ruidosa
    return x_t + np.random.normal(loc=0, scale=1, size=x_t.shape)

# Número de partículas
num_particulas = 1000

# Generar partículas iniciales aleatorias
particulas = np.random.uniform(low=0, high=10, size=(num_particulas, 1))

# Iterar sobre las observaciones
for observacion in observaciones:
    # Muestrear nuevas partículas a partir de las existentes utilizando la función de transición de estado
    nuevas_particulas = transicion_estado(particulas)
    
    # Calcular los pesos de las partículas basados en las observaciones
    pesos = observacion_modelo(observacion) - nuevas_particulas
    
    # Normalizar los pesos
    pesos = np.exp(-0.5 * (pesos ** 2))
    pesos /= np.sum(pesos)
    
    # Muestrear partículas basadas en sus pesos
    indices = np.random.choice(np.arange(num_particulas), size=num_particulas, p=pesos.flatten())
    particulas = nuevas_particulas[indices]
    
# Estimar el estado del sistema utilizando las partículas finales (por ejemplo, promedio de las partículas)
estado_estimado = np.mean(particulas)

print("Estado estimado del sistema:", estado_estimado)
 covarianza:", filtro.P)