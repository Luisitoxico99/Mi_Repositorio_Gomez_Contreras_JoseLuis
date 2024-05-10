class SistemaExpertoMedico:
    def __init__(self, reglas_diagnosticas, reglas_causales):
        self.reglas_diagnosticas = reglas_diagnosticas
        self.reglas_causales = reglas_causales

    def diagnosticar_enfermedad(self, sintomas):
        enfermedades = set()
        for regla in self.reglas_diagnosticas:
            if regla.cumple_condiciones(sintomas):
                enfermedades.update(regla.enfermedades)
        return enfermedades

    def inferir_causas(self, enfermedad):
        causas = set()
        for regla in self.reglas_causales:
            if enfermedad in regla.enfermedades:
                causas.update(regla.causas)
        return causas

class ReglaDiagnostica:
    def __init__(self, condiciones, enfermedades):
        self.condiciones = condiciones
        self.enfermedades = enfermedades

    def cumple_condiciones(self, sintomas):
        return all(condicion in sintomas for condicion in self.condiciones)

class ReglaCausal:
    def __init__(self, enfermedades, causas):
        self.enfermedades = enfermedades
        self.causas = causas

# Ejemplo de uso
reglas_diagnosticas = [
    ReglaDiagnostica(["fiebre", "tos"], {"Resfriado"}),
    ReglaDiagnostica(["dolor_de_cabeza", "fiebre"], {"Gripe"})
]

reglas_causales = [
    ReglaCausal({"Resfriado"}, {"Virus del resfriado"}),
    ReglaCausal({"Gripe"}, {"Virus de la gripe"})
]

sintomas = ["fiebre", "tos"]

sistema_experto = SistemaExpertoMedico(reglas_diagnosticas, reglas_causales)
enfermedades_diagnosticadas = sistema_experto.diagnosticar_enfermedad(sintomas)
print("Enfermedades diagnosticadas:", enfermedades_diagnosticadas)

for enfermedad in enfermedades_diagnosticadas:
    causas = sistema_experto.inferir_causas(enfermedad)
    print(f"Causas de {enfermedad}: {causas}")
