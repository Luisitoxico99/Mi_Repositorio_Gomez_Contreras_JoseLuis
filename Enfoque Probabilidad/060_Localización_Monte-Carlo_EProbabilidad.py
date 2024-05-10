import numpy as np
import matplotlib.pyplot as plt

# Función para generar partículas aleatorias
def generar_particulas(n_particulas, limite_x, limite_y):
    particulas = []
    for _ in range(n_particulas):
        x = np.random.uniform(0, limite_x)
        y = np.random.uniform(0, limite_y)
        particulas.append([x, y, 1/n_particulas])  # Inicialmente, todas las partículas tienen el mismo peso
    return np.array(particulas)

# Función para mover las partículas basado en la velocidad y dirección del robot
def mover_particulas(particulas, velocidad, direccion, limite_x, limite_y):
    for i in range(len(particulas)):
        particulas[i][0] += velocidad * np.cos(direccion)
        particulas[i][1] += velocidad * np.sin(direccion)
        # Mantener las partículas dentro de los límites del entorno
        particulas[i][0] = np.clip(particulas[i][0], 0, limite_x)
        particulas[i][1] = np.clip(particulas[i][1], 0, limite_y)
    return particulas

# Función para calcular la probabilidad de observación dada la posición estimada del robot
def calcular_probabilidad_observacion(particulas, observacion):
    sigma = 1.0  # Desviación estándar del sensor
    for i in range(len(particulas)):
        dx = part[i][0] - observacion[0]
        dy = part[i][1] - observacion[1]
        distancia = np.sqrt(dx**2 + dy**2)
        # Asignar un peso a cada partícula basado en la probabilidad de observación
        particulas[i][2] *= np.exp(-0.5 * (distancia / sigma)**2)
    # Normalizar los pesos de las partículas para que sumen 1
    total = np.sum(particulas[:, 2])
    particulas[:, 2] /= total
    return particulas

# Función para estimar la posición del robot utilizando las partículas y sus pesos
def estimar_posicion(particulas):
    x_estimado = np.average(particulas[:, 0], weights=particulas[:, 2])
    y_estimado = np.average(particulas[:, 1], weights=particulas[:, 2])
    return x_estimado, y_estimado

# Parámetros del entorno y el robot
limite_x = 100
limite_y = 100
velocidad = 1.0
direccion = np.pi / 4  # 45 grados en radianes

# Generar partículas aleatorias
n_particulas = 100
particulas = generar_particulas(n_particulas, limite_x, limite_y)

# Observación del robot (posición conocida en este ejemplo)
observacion = [20, 30]

# Mover las partículas basado en la velocidad y dirección del robot
particulas = mover_particulas(particulas, velocidad, direccion, limite_x, limite_y)

# Calcular la probabilidad de observación dada la posición estimada del robot
particulas = calcular_probabilidad_observacion(particulas, observacion)

# Estimar la posición del robot utilizando las partículas y sus pesos
x_estimado, y_estimado = estimar_posicion(particulas)

# Visualizar las partículas y la posición estimada del robot
plt.scatter(particulas[:, 0], particulas[:, 1], c=particulas[:, 2], cmap='jet', marker='o')
plt.colorbar(label='Pesos de las partículas')
plt.scatter(observacion[0], observacion[1], color='red', marker='x', label='Observación')
plt.scatter(x_estimado, y_estimado, color='green', marker='o', label='Posición estimada')
plt.xlabel('Coordenada X')
plt.ylabel('Coordenada Y')
plt.title('Localización utilizando Filtro de Partículas (Monte Carlo)')
plt.legend()
plt.grid(True)
plt.axis([0, limite_x, 0, limite_y])
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
