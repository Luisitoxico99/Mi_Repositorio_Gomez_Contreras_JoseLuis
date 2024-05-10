import time

class SensorUltrasonido:
    def __init__(self):
        self.distancia = 0
    
    def medir_distancia(self):
        # Simular la medición de distancia
        self.distancia = 10  # Supongamos que la distancia medida es 10 cm
        return self.distancia

class ActuadorMovimiento:
    def mover_adelante(self):
        print("Moviendo hacia adelante")
    
    def mover_atras(self):
        print("Moviendo hacia atrás")
    
    def girar(self):
        print("Girando")

# Inicializar el sensor de ultrasonido y el actuador de movimiento
sensor = SensorUltrasonido()
actuador = ActuadorMovimiento()

# Ciclo principal del robot
while True:
    # Medir la distancia utilizando el sensor de ultrasonido
    distancia = sensor.medir_distancia()
    
    # Si la distancia es menor que 20 cm, moverse hacia atrás y girar
    if distancia < 20:
        actuador.mover_atras()
        actuador.girar()
        time.sleep(1)  # Esperar 1 segundo para evitar la detección múltiple de obstáculos
    
    # Si la distancia es mayor o igual a 20 cm, moverse hacia adelante
    else:
        actuador.mover_adelante()
    
    time.sleep(0.5)  # Esperar 0.5 segundos antes de la próxima medición
