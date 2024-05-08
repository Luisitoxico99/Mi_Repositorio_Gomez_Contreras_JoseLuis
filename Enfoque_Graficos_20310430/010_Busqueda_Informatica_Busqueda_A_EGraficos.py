import heapq

def astar(graph, start, goal, heuristic):
    frontier = [(0, start)]  # (costo acumulado + heurística, nodo)
    came_from = {}
    cost_so_far = {start: 0}

    while frontier:
        _, current_node = heapq.heappop(frontier)

        if current_node == goal:
            break

        for next_node, cost in graph[current_node].items():
            new_cost = cost_so_far[current_node] + cost
            if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                cost_so_far[next_node] = new_cost
                priority = new_cost + heuristic(next_node, goal)
                heapq.heappush(frontier, (priority, next_node))
                came_from[next_node] = current_node

    # Reconstruir el camino
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()

    return path

# Ejemplo de una heurística de distancia Euclidiana en un grafo bidimensional
def euclidean_distance(node, goal):
    x1, y1 = node
    x2, y2 = goal
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

# Grafo de ejemplo representado como un diccionario de diccionarios
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'D': 5, 'E': 1},
    'C': {'A': 2, 'D': 8},
    'D': {'B': 5, 'C': 8},
    'E': {'B': 1}
}

# Nodo de inicio y nodo objetivo para la búsqueda
start_node = 'A'
goal_node = 'E'

# Llamamos a la búsqueda A* con la heurística de distancia Euclidiana
path = astar(graph, start_node, goal_node, euclidean_distance)

# Imprimimos el camino encontrado
print("Camino encontrado por A*:", path)
