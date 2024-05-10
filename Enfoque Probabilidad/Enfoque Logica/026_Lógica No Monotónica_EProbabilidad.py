class LogicaNoMonotonica:
    def __init__(self, creencias):
        self.creencias = creencias

    def agregar_creencia(self, nueva_creencia):
        # Agregar una nueva creencia a la lista de creencias
        self.creencias.append(nueva_creencia)

    def revisar_creencias(self):
        # Realizar una revisión de creencias basada en ciertas reglas o criterios
        # Aquí podrías implementar lógica específica para determinar qué creencias se deben revisar o retractar
        pass

# Ejemplo de uso
creencias_iniciales = ["p", "q"]
logica_no_monotonica = LogicaNoMonotonica(creencias_iniciales)

# Agregar una nueva creencia
nueva_creencia = "r"
logica_no_monotonica.agregar_creencia(nueva_creencia)

# Revisar las creencias
logica_no_monotonica.revisar_creencias()
