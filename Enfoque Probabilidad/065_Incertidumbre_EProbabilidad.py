import numpy as np
import matplotlib.pyplot as plt

# Parámetros del péndulo
m = 1  # Masa del péndulo
l = 1  # Longitud del péndulo
g = 9.81  # Aceleración debida a la gravedad

# Parámetros del controlador PID
Kp = 100  # Ganancia proporcional
Ki = 10   # Ganancia integral
Kd = 10   # Ganancia derivativa

# Condiciones iniciales
theta_0 = np.pi / 4  # Ángulo inicial del péndulo
theta_dot_0 = 0      # Velocidad angular inicial del péndulo

# Tiempo de simulación
dt = 0.01   # Paso de tiempo
t_total = 10  # Tiempo total de simulación

# Función de control PID
def pid_control(theta, theta_dot):
    error = 0 - theta  # Error: mantener el péndulo en posición vertical (0 grados)
    integral = np.trapz(error) * dt  # Integral del error
    derivative = np.diff(error) / dt  # Derivada del error
    control = Kp * error + Ki * integral + Kd * derivative
    return control

# Simulación de la dinámica del péndulo con control PID
t = np.arange(0, t_total, dt)
theta = np.zeros_like(t)
theta_dot = np.zeros_like(t)

theta[0] = theta_0
theta_dot[0] = theta_dot_0

for i in range(1, len(t)):
    control = pid_control(theta[i-1], theta_dot[i-1])
    theta_ddot = (m * g * l * np.sin(theta[i-1]) + control) / (m * l**2)
    theta_dot[i] = theta_dot[i-1] + theta_ddot * dt
    theta[i] = theta[i-1] + theta_dot[i] * dt

# Graficar resultados
plt.figure(figsize=(10, 6))
plt.plot(t, theta, label='Ángulo')
plt.xlabel('Tiempo (s)')
plt.ylabel('Ángulo (rad)')
plt.title('Control PID de un Péndulo Invertido')
plt.grid(True)
plt.legend()
plt.show()
