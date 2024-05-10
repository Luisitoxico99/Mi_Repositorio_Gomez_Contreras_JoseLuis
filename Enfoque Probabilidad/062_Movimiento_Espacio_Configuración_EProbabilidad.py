import matplotlib.pyplot as plt
import numpy as np

# Definir los límites del espacio de configuración
x_min, x_max = 0, 10
y_min, y_max = 0, 10
theta_min, theta_max = 0, 2*np.pi

# Crear una cuadrícula de puntos en el espacio de configuración
n_points = 100
x = np.linspace(x_min, x_max, n_points)
y = np.linspace(y_min, y_max, n_points)
theta = np.linspace(theta_min, theta_max, n_points)

# Graficar el espacio de configuración
plt.figure(figsize=(8, 6))
plt.plot([x_min, x_min, x_max, x_max, x_min], [y_min, y_max, y_max, y_min, y_min], 'k--')
plt.xlabel('Coordenada X')
plt.ylabel('Coordenada Y')
plt.title('Espacio de Configuración')
plt.grid(True)

# Mostrar la orientación del robot en el espacio de configuración
for i in range(len(x)):
    for j in range(len(y)):
        plt.arrow(x[i], y[j], np.cos(theta), np.sin(theta), head_width=0.1, head_length=0.1, fc='r', ec='r')

plt.show()
