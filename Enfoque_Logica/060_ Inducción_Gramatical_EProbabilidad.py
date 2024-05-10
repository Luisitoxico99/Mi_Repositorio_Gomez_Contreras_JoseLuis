class InduccionGramatical:
    def __init__(self, ejemplos):
        self.ejemplos = ejemplos
        self.gramatica = {}

    def inducir(self):
        for ejemplo in self.ejemplos:
            for i in range(len(ejemplo)):
                for j in range(i + 1, len(ejemplo) + 1):
                    subcadena = ejemplo[i:j]
                    if subcadena not in self.gramatica:
                        self.gramatica[subcadena] = 1
                    else:
                        self.gramatica[subcadena] += 1
        return self.construir_gramatica()

    def construir_gramatica(self):
        reglas_gramatica = []
        for subcadena, frecuencia in self.gramatica.items():
            reglas_gramatica.append(subcadena)
        return reglas_gramatica

# Ejemplo de uso
ejemplos = ["abc", "abbc", "aabbcc"]
inductor = InduccionGramatical(ejemplos)
gramatica = inductor.inducir()
print("Gramática inducida:", gramatica)
