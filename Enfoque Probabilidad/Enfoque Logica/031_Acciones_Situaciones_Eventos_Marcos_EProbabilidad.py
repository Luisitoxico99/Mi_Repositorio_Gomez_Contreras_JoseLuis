class Marco:
    def __init__(self, nombre):
        self.nombre = nombre
        self.atributos = {}

    def agregar_atributo(self, nombre, valor):
        self.atributos[nombre] = valor

    def obtener_atributo(self, nombre):
        return self.atributos.get(nombre)

# Definimos un marco para representar una acción
accion_comer = Marco("Comer")
accion_comer.agregar_atributo("Tipo", "Fisiológica")
accion_comer.agregar_atributo("Descripcion", "Ingerir alimentos para obtener nutrientes")

# Definimos un marco para representar una situación
situacion_hambre = Marco("Hambre")
situacion_hambre.agregar_atributo("Tipo", "Fisiológica")
situacion_hambre.agregar_atributo("Descripcion", "Sensación de necesidad de alimentarse")

# Definimos un marco para representar un evento
evento_desayuno = Marco("Desayuno")
evento_desayuno.agregar_atributo("Tipo", "Rutinario")
evento_desayuno.agregar_atributo("Descripcion", "Primera comida del día")

# Función para imprimir un marco
def imprimir_marco(marco):
    print("Nombre:", marco.nombre)
    print("Atributos:")
    for nombre, valor in marco.atributos.items():
        print(f" - {nombre}: {valor}")

# Imprimimos los marcos
print("Accion:")
imprimir_marco(accion_comer)
print("\nSituacion:")
imprimir_marco(situacion_hambre)
print("\nEvento:")
imprimir_marco(evento_desayuno)
