class Formula:
    def __init__(self, cuantificador, variable, predicado):
        self.cuantificador = cuantificador  # Cuantificador (universal o existencial)
        self.variable = variable  # Variable cuantificada
        self.predicado = predicado  # Predicado que depende de la variable

    def skolemizar(self):
        if self.cuantificador == '∃':  # Si el cuantificador es existencial
            # Introducimos una nueva función de Skolem que depende de las variables universales
            # Aquí podrías personalizar la función de Skolem según tus necesidades
            funcion_skolem = 'f(' + self.variable + ')'
            # Reemplazamos la variable existencial con la función de Skolem en el predicado
            nuevo_predicado = self.predicado.replace(self.variable, funcion_skolem)
            return nuevo_predicado
        else:
            return self.predicado  # Si el cuantificador es universal, no hay cambios

# Ejemplo de uso
formula_original = Formula('∀', 'x', 'R(x, y)')
formula_skolemizada = formula_original.skolemizar()

print("Fórmula original:", formula_original.predicado)
print("Fórmula skolemizada:", formula_skolemizada)
