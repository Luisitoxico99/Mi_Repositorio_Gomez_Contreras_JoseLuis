class FormulaDifusa:
    def __init__(self, predicado, grado):
        self.predicado = predicado
        self.grado = grado

    def mostrar_formula(self):
        return f"{self.predicado}({self.grado})"

# Ejemplo de uso
formula_difusa = FormulaDifusa("alto", 0.8)
print("Fórmula difusa:", formula_difusa.mostrar_formula())
