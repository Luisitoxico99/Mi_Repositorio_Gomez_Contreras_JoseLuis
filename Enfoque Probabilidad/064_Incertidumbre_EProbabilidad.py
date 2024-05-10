import numpy as np
import matplotlib.pyplot as plt

# Definir las matrices del modelo dinámico (matrices de transición)
A = np.array([[1, 1], [0, 1]])  # Modelo de movimiento: posición y velocidad
B = np.array([[0.5], [1]])  # Modelo de control: aceleración (en este caso, controlamos directamente la velocidad)
H = np.array([[1, 0]])  # Modelo de observación: solo podemos observar la posición

# Definir la matriz de covarianza del proceso (covarianza del ruido del proceso)
Q = np.array([[0.1, 0], [0, 0.1]])  # Covarianza del ruido del proceso (asumimos que el ruido es independiente)

# Definir la matriz de covarianza de la medición (covarianza del ruido de la medición)
R = np.array([[1]])  # Covarianza del ruido de la medición (varianza de la medición)

# Inicializar el estado inicial y la covarianza inicial
x_0 = np.array([[0], [0]])  # Estado inicial: posición y velocidad
P_0 = np.array([[1, 0], [0, 1]])  # Covarianza inicial

# Simular el sistema
T = 100  # Número de pasos de tiempo
dt = 1  # Intervalo de tiempo entre pasos (segundos)

# Generar datos de control (en este caso, la aceleración constante)
u = np.ones((T, 1)) * 0.1  # Aceleración constante

# Simular el proceso y la medición (añadiendo ruido)
true_state = []
measurements = []
for t in range(T):
    # Actualizar el estado verdadero del sistema (usando el modelo dinámico y el control)
    x_true = np.dot(A, true_state[-1]) + np.dot(B, u[t]) if len(true_state) > 0 else x_0
    true_state.append(x_true)
    
    # Generar la medición (observación)
    z = np.dot(H, x_true) + np.random.normal(0, np.sqrt(R))  # Agregar ruido a la medición
    measurements.append(z)

# Implementar el filtro de Kalman
x_est = x_0  # Inicializar la estimación del estado
P_est = P_0  # Inicializar la covarianza de la estimación

estimated_states = []
for t in range(T):
    # Predicción del estado siguiente
    x_pred = np.dot(A, x_est) + np.dot(B, u[t])
    P_pred = np.dot(np.dot(A, P_est), A.T) + Q
    
    # Actualización basada en la medición
    K = np.dot(np.dot(P_pred, H.T), np.linalg.inv(np.dot(np.dot(H, P_pred), H.T) + R))
    x_est = x_pred + np.dot(K, (measurements[t] - np.dot(H, x_pred)))
    P_est = np.dot((np.eye(2) - np.dot(K, H)), P_pred)
    
    # Guardar la estimación del estado actual
    estimated_states.append(x_est)

# Extraer la posición y la velocidad estimadas
estimated_positions = [x[0] for x in estimated_states]
estimated_velocities = [x[1] for x in estimated_states]

# Graficar los resultados
plt.figure(figsize=(10, 6))
plt.plot(range(T), [x[0] for x in true_state], label='Estado Verdadero', color='blue')
plt.plot(range(T), estimated_positions, label='Estado Estimado', color='red')
plt.xlabel('Tiempo')
plt.ylabel('Posición')
plt.title('Filtro de Kalman: Posición Estimada vs. Posición Verdadera')
plt.legend()
plt.grid(True)
plt.show()
