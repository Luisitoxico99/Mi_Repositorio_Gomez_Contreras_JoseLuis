from pyhopfield import HopfieldNetwork
import numpy as np

# Crear una red de Hopfield con 100 neuronas
red_hopfield = HopfieldNetwork(100)

# Patrones de entrenamiento (patrón de puntos aleatorios)
patron1 = np.random.choice([-1, 1], size=(100,))
patron2 = np.random.choice([-1, 1], size=(100,))

# Entrenar la red de Hopfield con los patrones de entrenamiento
red_hopfield.train([patron1, patron2])

# Estado inicial (ruido) para recuperar
estado_inicial = np.random.choice([-1, 1], size=(100,))

# Recuperar el patrón más cercano al estado inicial
patron_recuperado = red_hopfield.recall(estado_inicial)

print("Patrón recuperado:", patron_recuperado)
