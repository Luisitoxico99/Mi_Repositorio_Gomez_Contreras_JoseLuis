class Estado:
    def __init__(self, x, y):
        self.x = x  # Posición x en el laberinto
        self.y = y  # Posición y en el laberinto

    def __eq__(self, otro):
        return self.x == otro.x and self.y == otro.y

    def __hash__(self):
        return hash((self.x, self.y))

class Accion:
    def __init__(self, nombre, dx, dy):
        self.nombre = nombre  # Nombre de la acción (moverse hacia arriba, abajo, izquierda, derecha)
        self.dx = dx  # Cambio en la posición x
        self.dy = dy  # Cambio en la posición y

class EspacioEstados:
    def __init__(self, laberinto):
        self.laberinto = laberinto
        self.acciones = [
            Accion("arriba", 0, -1),
            Accion("abajo", 0, 1),
            Accion("izquierda", -1, 0),
            Accion("derecha", 1, 0)
        ]

    def obtener_sucesores(self, estado):
        sucesores = []
        for accion in self.acciones:
            nuevo_x = estado.x + accion.dx
            nuevo_y = estado.y + accion.dy
            # Verificar si la nueva posición está dentro del laberinto y no es un obstáculo
            if 0 <= nuevo_x < len(self.laberinto[0]) and 0 <= nuevo_y < len(self.laberinto) and self.laberinto[nuevo_y][nuevo_x] != 1:
                sucesores.append(Estado(nuevo_x, nuevo_y))
        return sucesores

# Ejemplo de uso
laberinto = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

espacio = EspacioEstados(laberinto)
estado_inicial = Estado(0, 0)
print("Sucesores del estado inicial:", espacio.obtener_sucesores(estado_inicial))
