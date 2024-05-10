class SistemaExperto:
    def __init__(self, base_conocimiento, hechos):
        self.base_conocimiento = base_conocimiento
        self.hechos = hechos

    def encadenamiento_hacia_atras(self, meta):
        if meta in self.hechos:
            return True
        for regla in self.base_conocimiento:
            if meta == regla.consecuente:
                if all(self.encadenamiento_hacia_atras(antecedente) for antecedente in regla.antecedente):
                    return True
        return False

# Ejemplo de uso
base_conocimiento = [
    Regla(["fiebre", "tos"], "Resfriado"),
    Regla(["dolor_de_cabeza", "fiebre"], "Gripe")
]
hechos = ["fiebre", "tos"]

sistema_experto = SistemaExperto(base_conocimiento, hechos)
tiene_fiebre = sistema_experto.encadenamiento_hacia_atras("fiebre")
print("¿El paciente tiene fiebre?", tiene_fiebre)
