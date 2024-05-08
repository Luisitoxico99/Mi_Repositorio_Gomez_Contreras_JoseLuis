dimport heapq

def greedy_best_first_search(graph, start, goal, heuristic):
    frontier = [(heuristic(start, goal), start)]
    explored = set()

    while frontier:
        _, current_node = heapq.heappop(frontier)

        if current_node == goal:
            return True  # Se encontró el objetivo

        explored.add(current_node)

        for neighbor in graph[current_node]:
            if neighbor not in explored:
                priority = heuristic(neighbor, goal)
                heapq.heappush(frontier, (priority, neighbor))

    return False  # No se encontró el objetivo

# Ejemplo de una heurística de distancia Euclidiana en un grafo bidimensional
def euclidean_distance(node, goal):
    x1, y1 = node
    x2, y2 = goal
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

# Grafo de ejemplo representado como un diccionario de listas de adyacencia
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Nodo de inicio y nodo objetivo para la búsqueda
start_node = 'A'
goal_node = 'F'

# Llamamos a la búsqueda voraz con la heurística de distancia Euclidiana
result = greedy_best_first_search(graph, start_node, goal_node, euclidean_distance)

# Imprimimos el resultado de la búsqueda
if result:
    print("¡Se encontró un camino entre", start_node, "y", goal_node, "!")
else:
    print("No se encontró un camino entre", start_node, "y", goal_node, ".")
