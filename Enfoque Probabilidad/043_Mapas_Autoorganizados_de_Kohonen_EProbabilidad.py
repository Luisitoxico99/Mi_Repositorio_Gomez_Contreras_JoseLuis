from minisom import MiniSom
import numpy as np

# Definir el tamaño del mapa SOM
tamano_mapa = (10, 10)  # Número de neuronas en el mapa SOM (10x10 en este caso)

# Crear una instancia de MiniSom
som = MiniSom(tamano_mapa[0], tamano_mapa[1], input_len=10, sigma=1.0, learning_rate=0.5)

# Inicializar los pesos del SOM
som.random_weights_init(data)

# Entrenar el SOM
som.train_random(data, 100)  # Entrenar el SOM con 100 iteraciones

# Obtener los pesos finales del SOM
pesos_finales = som.get_weights()

# Visualizar el mapa SOM
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 10))
for x, row in enumerate(pesos_finales):
    for y, weight in enumerate(row):
        plt.text(x, y, str(np.argmax(weight)), color=plt.cm.gray(weight / np.max(pesos_finales)))
plt.xticks(np.arange(tamano_mapa[0]))
plt.yticks(np.arange(tamano_mapa[1]))
plt.grid()
plt.show()
