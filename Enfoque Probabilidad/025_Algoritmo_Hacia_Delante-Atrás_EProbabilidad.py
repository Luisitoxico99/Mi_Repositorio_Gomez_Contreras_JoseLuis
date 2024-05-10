from hmmlearn import hmm
import numpy as np

# Datos observados
observaciones = np.array([[1], [2], [3], [4], [5]])

# Definir y entrenar el modelo HMM
modelo = hmm.GaussianHMM(n_components=2, covariance_type="full", n_iter=100)
modelo.fit(observaciones)

# Calcular las probabilidades hacia adelante (Forward probabilities)
forward_probabilidades = modelo.forward(observaciones)

# Calcular las probabilidades hacia atrás (Backward probabilities)
backward_probabilidades = modelo.backward(observaciones)

# Calcular las probabilidades combinadas
# La probabilidad combinada es el producto elemento por elemento de las probabilidades hacia adelante y hacia atrás
combined_probabilidades = forward_probabilidades * backward_probabilidades

# Normalizar las probabilidades combinadas
normalized_probabilidades = combined_probabilidades / np.sum(combined_probabilidades, axis=1, keepdims=True)

print("Probabilidades combinadas normalizadas:", normalized_probabilidades)
