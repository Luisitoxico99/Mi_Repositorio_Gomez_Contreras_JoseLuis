from filterpy.kalman import KalmanFilter
import numpy as np

# Definir el filtro de Kalman
filtro = KalmanFilter(dim_x=2, dim_z=1)

# Definir la matriz de transición de estado (A)
filtro.F = np.array([[1., 1.],
                     [0., 1.]])

# Definir la matriz de observación (H)
filtro.H = np.array([[1., 0.]])

# Definir las matrices de covarianza del proceso y de la medición (Q y R)
filtro.Q *= 0.01
filtro.R *= 0.1

# Definir la estimación inicial del estado y de la covarianza
filtro.x = np.array([[0.],
                     [0.]])
filtro.P *= 0.01

# Simular mediciones ruidosas
mediciones = np.random.normal(loc=0., scale=0.1, size=(50, 1))

# Inicializar listas para guardar las estimaciones de estado
estimaciones_estado = []
estimaciones_covarianza = []

# Actualizar el filtro de Kalman con cada medición
for medida in mediciones:
    filtro.predict()
    filtro.update(medida)
    estimaciones_estado.append(filtro.x)
    estimaciones_covarianza.append(filtro.P)

# Imprimir las estimaciones finales del estado y la covarianza
print("Estimación final del estado:", filtro.x)
print("Estimación final de la covarianza:", filtro.P)