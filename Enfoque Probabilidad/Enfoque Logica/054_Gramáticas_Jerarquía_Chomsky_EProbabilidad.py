clclass Tipo0:
    def __init__(self, reglas):
        self.reglas = reglas  # Lista de reglas de producción

    def generar_lenguaje(self):
        # Aquí podríamos implementar un generador para el lenguaje
        pass

class Tipo1:
    def __init__(self, reglas):
        self.reglas = reglas  # Lista de reglas de producción

    def generar_lenguaje(self):
        # Aquí podríamos implementar un generador para el lenguaje
        pass

class Tipo2:
    def __init__(self, reglas):
        self.reglas = reglas  # Lista de reglas de producción

    def generar_lenguaje(self):
        # Aquí podríamos implementar un generador para el lenguaje
        pass

class Tipo3:
    def __init__(self, reglas):
        self.reglas = reglas  # Lista de reglas de producción

    def generar_lenguaje(self):
        # Aquí podríamos implementar un generador para el lenguaje
        pass

# Ejemplo de uso
# Supongamos que tenemos algunas reglas de producción para cada tipo de gramática
tipo0 = Tipo0(["S -> aSb", "S -> ε"])
tipo1 = Tipo1(["AB -> BA", "Aa -> aa", "Ba -> ab"])
tipo2 = Tipo2(["S -> AB", "A -> a", "B -> b"])
tipo3 = Tipo3(["S -> aS", "S -> b"])

# Podemos generar lenguajes utilizando estas gramáticas
print("Lenguaje generado por Tipo 0:", tipo0.generar_lenguaje())
print("Lenguaje generado por Tipo 1:", tipo1.generar_lenguaje())
print("Lenguaje generado por Tipo 2:", tipo2.generar_lenguaje())
print("Lenguaje generado por Tipo 3:", tipo3.generar_lenguaje())
