# Definimos la función para la búsqueda en profundidad iterativa
def iddfs(graph, start, goal, max_depth):
    # Iteramos desde la profundidad 0 hasta la profundidad máxima
    for depth in range(max_depth + 1):
        # Llamamos a la función DFS limitando la profundidad actual
        found = dfs(graph, start, goal, depth)
        
        # Si encontramos el objetivo, devolvemos True
        if found:
            return True
    
    # Si no encontramos el objetivo dentro de la profundidad máxima, devolvemos False
    return False

# Definimos la función para la búsqueda en profundidad limitada (DFS)
def dfs(graph, node, goal, depth, visited=None):
    # Si no se ha proporcionado un conjunto de nodos visitados, lo creamos
    if visited is None:
        visited = set()
    
    # Añadimos el nodo actual a los nodos visitados
    visited.add(node)
    
    # Si hemos alcanzado el objetivo o la profundidad máxima, devolvemos True
    if node == goal or depth == 0:
        return node == goal
    
    # Si no hemos alcanzado el objetivo ni la profundidad máxima, continuamos la búsqueda
    for neighbor in graph[node]:
        if neighbor not in visited:
            if dfs(graph, neighbor, goal, depth - 1, visited):
                return True
    
    # Si no se encontró el objetivo en esta rama, devolvemos False
    return False

# Grafo de ejemplo representado como un diccionario
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

# Profundidad máxima para la búsqueda en profundidad iterativa
max_depth = 3

