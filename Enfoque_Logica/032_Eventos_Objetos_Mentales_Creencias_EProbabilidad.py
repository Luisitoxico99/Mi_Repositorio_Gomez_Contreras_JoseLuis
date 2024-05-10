class Creencia:
    def __init__(self, contenido, confianza=1.0):
        self.contenido = contenido  # Contenido de la creencia
        self.confianza = confianza  # Nivel de confianza en la creencia

# Crear algunas creencias
creencia1 = Creencia("El cielo está despejado")
creencia2 = Creencia("Mañana lloverá", confianza=0.8)
creencia3 = Creencia("Los gatos son mamíferos", confianza=0.9)

# Función para imprimir una creencia
def imprimir_creencia(creencia):
    print("Contenido:", creencia.contenido)
    print("Confianza:", creencia.confianza)

# Imprimir las creencias
print("Creencia 1:")
imprimir_creencia(creencia1)
print("\nCreencia 2:")
imprimir_creencia(creencia2)
print("\nCreencia 3:")
imprimir_creencia(creencia3)
