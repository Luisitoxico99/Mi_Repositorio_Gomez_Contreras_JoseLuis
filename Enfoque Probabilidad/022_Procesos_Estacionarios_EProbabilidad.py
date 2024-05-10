import numpy as np
import matplotlib.pyplot as plt

# Parámetros del proceso estacionario
num_muestras = 1000  # Número de muestras a generar
media = 0  # Media del proceso estacionario
varianza = 1  # Varianza del proceso estacionario

# Generar muestras de un proceso estacionario débil (ruido blanco)
muestras = np.random.normal(loc=media, scale=np.sqrt(varianza), size=num_muestras)

# Visualizar las muestras generadas
plt.figure(figsize=(10, 5))
plt.plot(muestras)
plt.title('Muestras de un Proceso Estacionario Débil (Ruido Blanco)')
plt.xlabel('Tiempo')
plt.ylabel('Valor')
plt.grid(True)
plt.show()
