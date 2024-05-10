class SistemaExperto:
    def __init__(self, base_conocimientos):
        self.base_conocimientos = base_conocimientos

    def inferir(self, hechos):
        while True:
            nueva_informacion = False
            for regla in self.base_conocimientos:
                if self.se_cumplen_las_condiciones(regla[0], hechos) and regla[1] not in hechos:
                    hechos.append(regla[1])
                    nueva_informacion = True
            if not nueva_informacion:
                break
        return hechos

    def se_cumplen_las_condiciones(self, condiciones, hechos):
        for condicion in condiciones:
            if condicion not in hechos:
                return False
        return True

# Base de conocimientos
base_conocimientos = [
    (["tiene_fiebre", "tiene_tos"], "resfriado"),
    (["tiene_fiebre", "dolor_de_garganta"], "amigdalitis")
]

# Crear sistema experto
sistema_experto = SistemaExperto(base_conocimientos)

# Realizar inferencia
hechos = ["tiene_fiebre", "tiene_tos"]
enfermedad = sistema_experto.inferir(hechos)
print("Enfermedad inferida:", enfermedad[-1])
