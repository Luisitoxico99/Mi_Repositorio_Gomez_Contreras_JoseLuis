import numpy as np

# Función para calcular la cinemática inversa de un robot 2-DOF
def cinemática_inversa_2dof(x, y, l1, l2):
    # Calcular la distancia del efector final al origen
    d = np.sqrt(x**2 + y**2)
    
    # Calcular el ángulo de la primera articulación (θ1)
    theta1 = np.arctan2(y, x)
    
    # Calcular el ángulo de la segunda articulación (θ2)
    cos_theta2 = (l1**2 + l2**2 - d**2) / (2 * l1 * l2)
    sin_theta2 = np.sqrt(1 - cos_theta2**2)
    theta2 = np.arctan2(sin_theta2, cos_theta2)
    
    return theta1, theta2

# Coordenadas objetivo del efector final
x_objetivo = 5
y_objetivo = 5

# Longitudes de los brazos del robot
longitud_brazo1 = 3
longitud_brazo2 = 3

# Calcular la cinemática inversa
theta1, theta2 = cinemática_inversa_2dof(x_objetivo, y_objetivo, longitud_brazo1, longitud_brazo2)

# Imprimir los ángulos de las articulaciones
print("Ángulo de la primera articulación (θ1):", np.degrees(theta1))
print("Ángulo de la segunda articulación (θ2):", np.degrees(theta2))
