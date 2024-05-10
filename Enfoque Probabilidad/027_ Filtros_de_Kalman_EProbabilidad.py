from hmmlearn import hmm
import numpy as np

# Datos de ejemplo: secuencia de observaciones
observaciones = np.array([[1], [2], [3], [4], [5]])

# Definir y entrenar el modelo HMM
modelo = hmm.GaussianHMM(n_components=2, covariance_type="full", n_iter=100)
modelo.fit(observaciones)

# Generar secuencia de estados ocultos
secuencia_estados, _ = modelo.decode(observaciones)

print("Secuencia de estados ocultos:", secuencia_estados)
