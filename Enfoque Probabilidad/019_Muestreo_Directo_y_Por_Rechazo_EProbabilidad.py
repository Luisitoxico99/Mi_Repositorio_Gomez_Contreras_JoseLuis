import numpy as np

# Definir una distribución de probabilidad discreta
valores = np.array([1, 2, 3, 4, 5])
probabilidades = np.array([0.1, 0.2, 0.3, 0.2, 0.2])

# Generar muestras directamente de la distribución de probabilidad
muestra_directa = np.random.choice(valores, size=1000, p=probabilidades)

# Imprimir las muestras generadas
print("Muestras generadas mediante muestreo directo:", muestra_directa)
