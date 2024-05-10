# Definición de la lógica de segundo orden
class LogicaSegundoOrden:
    def __init__(self):
        self.preds = {}  # Predicados
        self.funcs = {}  # Funciones

    def agregar_predicado(self, nombre, aridad):
        self.preds[nombre] = aridad

    def agregar_funcion(self, nombre, aridad):
        self.funcs[nombre] = aridad

# Ejemplo de uso
logica = LogicaSegundoOrden()

# Agregar predicados y funciones
logica.agregar_predicado("Hijo", 2)
logica.agregar_predicado("Padre", 2)
logica.agregar_funcion("PadreDe", 1)

# Consultar la lógica de segundo orden
print("Predicados:", logica.preds)
print("Funciones:", logica.funcs)
