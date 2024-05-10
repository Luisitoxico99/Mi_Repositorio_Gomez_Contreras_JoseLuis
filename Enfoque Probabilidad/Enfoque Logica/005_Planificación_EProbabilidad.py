import heapq

class Estado:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, otro_estado):
        return self.x == otro_estado.x and self.y == otro_estado.y

    def __hash__(self):
        return hash((self.x, self.y))

class Nodo:
    def __init__(self, estado, g=0, h=0):
        self.estado = estado
        self.g = g  # Costo real desde el nodo inicial hasta este nodo
        self.h = h  # Heurística estimada desde este nodo hasta el objetivo

    def f(self):
        return self.g + self.h

class Planificador:
    def __init__(self, entorno, inicio, objetivo):
        self.entorno = entorno
        self.inicio = inicio
        self.objetivo = objetivo

    def encontrar_camino(self):
        abiertos = []
        cerrados = set()

        # Función heurística: distancia Manhattan
        def heuristica(actual, objetivo):
            return abs(actual.x - objetivo.x) + abs(actual.y - objetivo.y)

        heapq.heappush(abiertos, (0, Nodo(self.inicio, 0, heuristica(self.inicio, self.objetivo))))

        while abiertos:
            _, nodo_actual = heapq.heappop(abiertos)

            if nodo_actual.estado == self.objetivo:
                return self.reconstruir_camino(nodo_actual)

            cerrados.add(nodo_actual.estado)

            for sucesor in self.obtener_sucesores(nodo_actual):
                if sucesor.estado in cerrados:
                    continue

                sucesor.g = nodo_actual.g + 1
                sucesor.h = heuristica(sucesor.estado, self.objetivo)
                heapq.heappush(abiertos, (sucesor.f(), sucesor))

        return None  # No se encontró camino

    def obtener_sucesores(self, nodo):
        sucesores = []

        movimientos = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Movimientos arriba, abajo, derecha, izquierda

        for dx, dy in movimientos:
            nuevo_x = nodo.estado.x + dx
            nuevo_y = nodo.estado.y + dy

            if self.es_valido(nuevo_x, nuevo_y):
                sucesores.append(Nodo(Estado(nuevo_x, nuevo_y)))

        return sucesores

    def es_valido(self, x, y):
        return 0 <= x < len(self.entorno) and 0 <= y < len(self.entorno[0]) and self.entorno[x][y] != 1

    def reconstruir_camino(self, nodo):
        camino = []
        while nodo:
            camino.append((nodo.estado.x, nodo.estado.y))
            nodo = nodo.padre
        return camino[::-1]

# Ejemplo de uso
entorno = [
    [0, 0, 0, 0],
    [0, 1, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 0, 0],
]

inicio = Estado(0, 0)
objetivo = Estado(3, 3)

planificador = Planificador(entorno, inicio, objetivo)
camino = planificador.encontrar_camino()

if camino:
    print("Camino encontrado:", camino)
else:
    print("No se encontró un camino válido.")
