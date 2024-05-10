class SistemaExperto:
    def __init__(self):
        self.reglas = []

    def agregar_regla(self, premisa, conclusion):
        self.reglas.append((premisa, conclusion))

    def inferir(self, conocimiento):
        for premisa, conclusion in self.reglas:
            if premisa in conocimiento:
                return conclusion
        return None

# Crear un sistema experto
sistema_experto = SistemaExperto()

# Agregar reglas al sistema
sistema_experto.agregar_regla("fiebre y dolor_de_garganta", "amigdalitis")
sistema_experto.agregar_regla("fiebre y tos", "resfriado")

# Conocimiento inicial del paciente
conocimiento_paciente = ["fiebre", "dolor_de_garganta"]

# Inferir enfermedad del paciente
enfermedad = sistema_experto.inferir(conocimiento_paciente)
print("Enfermedad del paciente:", enfermedad)
