import numpy as np

# Definir la distribución de probabilidad objetivo
def p(x):
    return np.exp(-x**2 / 2) / np.sqrt(2 * np.pi)

# Definir la propuesta de transición (una distribución normal con desviación estándar sigma)
def q(x, sigma):
    return np.random.normal(x, sigma)

# Parámetros del algoritmo
sigma = 1  # Desviación estándar de la distribución de propuesta
num_muestras = 10000  # Número de muestras a generar
x_actual = 0  # Valor inicial de la cadena de Markov

# Generar muestras utilizando el algoritmo de Metropolis-Hastings
muestras = []
for _ in range(num_muestras):
    # Propuesta de transición
    x_propuesto = q(x_actual, sigma)
    # Calcular la razón de aceptación
    alpha = min(1, p(x_propuesto) / p(x_actual))
    # Aceptar o rechazar la propuesta
    if np.random.uniform(0, 1) < alpha:
        x_actual = x_propuesto
    # Agregar la muestra a la lista
    muestras.append(x_actual)

# Imprimir las muestras generadas
print("Muestras generadas mediante MCMC (Metropolis-Hastings):", muestras)
