class BaseConocimiento:
    def __init__(self):
        self.hechos = []
        self.reglas = []

    def agregar_hecho(self, hecho):
        self.hechos.append(hecho)

    def agregar_regla(self, regla):
        self.reglas.append(regla)

class Hecho:
    def __init__(self, predicado, argumentos):
        self.predicado = predicado
        self.argumentos = argumentos

    def __str__(self):
        return f"{self.predicado}({', '.join(self.argumentos)})"

class Regla:
    def __init__(self, antecedente, consecuente):
        self.antecedente = antecedente
        self.consecuente = consecuente

    def __str__(self):
        antecedente_str = ", ".join([str(hecho) for hecho in self.antecedente])
        consecuente_str = str(self.consecuente)
        return f"Si {antecedente_str}, entonces {consecuente_str}"

# Ejemplo de uso
base_conocimiento = BaseConocimiento()

# Agregar hechos a la base de conocimiento
base_conocimiento.agregar_hecho(Hecho("es_un_mamifero", ["perro"]))
base_conocimiento.agregar_hecho(Hecho("es_un_mamifero", ["gato"]))
base_conocimiento.agregar_hecho(Hecho("es_un_animal", ["perro"]))
base_conocimiento.agregar_hecho(Hecho("es_un_animal", ["gato"]))

# Agregar reglas a la base de conocimiento
base_conocimiento.agregar_regla(Regla([Hecho("es_un_mamifero", ["?x"])], Hecho("es_un_animal", ["?x"])))

# Consultar la base de conocimiento
print("Hechos:")
for hecho in base_conocimiento.hechos:
    print("-", hecho)

print("\nReglas:")
for regla in base_conocimiento.reglas:
    print("-", regla)
