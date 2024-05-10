class Categoria:
    def __init__(self, nombre, subcategorias=None):
        self.nombre = nombre
        self.subcategorias = subcategorias if subcategorias is not None else []

    def agregar_subcategoria(self, subcategoria):
        self.subcategorias.append(subcategoria)


# Definimos las categorías de la taxonomía
animalia = Categoria("Animalia")
mamiferos = Categoria("Mamíferos")
aves = Categoria("Aves")
reptiles = Categoria("Reptiles")

# Agregamos subcategorías a la categoría Animalia
animalia.agregar_subcategoria(mamiferos)
animalia.agregar_subcategoria(aves)
animalia.agregar_subcategoria(reptiles)

# Definimos algunos objetos en las categorías
gato = Categoria("Gato")
perro = Categoria("Perro")
ballena = Categoria("Ballena")

mamiferos.agregar_subcategoria(gato)
mamiferos.agregar_subcategoria(perro)
mamiferos.agregar_subcategoria(ballena)

aguila = Categoria("Águila")
pinguino = Categoria("Pingüino")
colibri = Categoria("Colibrí")

aves.agregar_subcategoria(aguila)
aves.agregar_subcategoria(pinguino)
aves.agregar_subcategoria(colibri)

cocodrilo = Categoria("Cocodrilo")
serpiente = Categoria("Serpiente")
lagartija = Categoria("Lagartija")

reptiles.agregar_subcategoria(cocodrilo)
reptiles.agregar_subcategoria(serpiente)
reptiles.agregar_subcategoria(lagartija)

# Función para imprimir la taxonomía
def imprimir_taxonomia(categoria, nivel=0):
    print("  " * nivel + categoria.nombre)
    for subcategoria in categoria.subcategorias:
        imprimir_taxonomia(subcategoria, nivel + 1)

# Imprimimos la taxonomía
imprimir_taxonomia(animalia)
