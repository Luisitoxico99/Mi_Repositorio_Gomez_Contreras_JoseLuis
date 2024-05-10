class Estado:from collections import defaultdict

class PlanificadorOrdenParcial:
    def __init__(self):
        self.grafo = defaultdict(list)  # Grafo para representar las relaciones de precedencia entre las tareas

    def agregar_tarea(self, tarea, precedentes=[]):
        for precedente in precedentes:
            self.grafo[precedente].append(tarea)

    def planificar(self):
        secuencia_ejecucion = []
        visitados = set()

        def dfs(tarea):
            if tarea not in visitados:
                visitados.add(tarea)
                for siguiente_tarea in self.grafo[tarea]:
                    dfs(siguiente_tarea)
                secuencia_ejecucion.append(tarea)

        for tarea in self.grafo.keys():
            dfs(tarea)

        return secuencia_ejecucion[::-1]

# Ejemplo de uso
planificador = PlanificadorOrdenParcial()
planificador.agregar_tarea('A', ['B', 'C'])
planificador.agregar_tarea('B', ['D'])
planificador.agregar_tarea('C', ['E'])
planificador.agregar_tarea('D', ['F'])
planificador.agregar_tarea('E')
planificador.agregar_tarea('F')

secuencia_ejecucion = planificador.planificar()
print("Secuencia de ejecución:", secuencia_ejecucion)
