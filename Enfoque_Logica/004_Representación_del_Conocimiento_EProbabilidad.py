class Marco:
    def __init__(self, atributos):
        self.atributos = atributos

    def mostrar_atributos(self):
        for atributo, valor in self.atributos.items():
            print(f"{atributo}: {valor}")

# Creación de un marco
perro = Marco({"especie": "canino", "raza": "labrador", "edad": 5})

# Mostrar atributos del marco
perro.mostrar_atributos()
