class SistemaExperto:
    def __init__(self, base_conocimiento):
        self.base_conocimiento = base_conocimiento

    def diagnosticar(self, sintomas):
        enfermedades = set()  # Creamos un conjunto para almacenar las enfermedades diagnosticadas
        for regla in self.base_conocimiento:  # Iteramos sobre todas las reglas en la base de conocimiento
            if regla.cumple_condiciones(sintomas):  # Verificamos si los síntomas cumplen las condiciones de la regla
                enfermedades.update(regla.enfermedades)  # Agregamos las enfermedades diagnosticadas por esta regla
        return enfermedades  # Devolvemos el conjunto de enfermedades diagnosticadas


class Regla:
    def __init__(self, condiciones, enfermedades):
        self.condiciones = condiciones  # Lista de síntomas requeridos para que se aplique la regla
        self.enfermedades = enfermedades  # Lista de enfermedades asociadas a la regla

    def cumple_condiciones(self, sintomas):
        return set(self.condiciones).issubset(sintomas)  # Verificamos si todos los síntomas están presentes


# Creamos una base de conocimiento con algunas reglas
base_conocimiento = [
    Regla(["fiebre", "tos"], {"Resfriado"}),
    Regla(["dolor_de_cabeza", "fiebre"], {"Gripe"})
]

# Creamos una instancia del sistema experto con la base de conocimiento
sistema_experto = SistemaExperto(base_conocimiento)

# Definimos los síntomas observados
sintomas = ["fiebre", "tos"]

# Llamamos al método de diagnóstico del sistema experto
enfermedades_diagnosticadas = sistema_experto.diagnosticar(sintomas)

# Imprimimos las enfermedades diagnosticadas
print("Enfermedades diagnosticadas:", enfermedades_diagnosticadas)
