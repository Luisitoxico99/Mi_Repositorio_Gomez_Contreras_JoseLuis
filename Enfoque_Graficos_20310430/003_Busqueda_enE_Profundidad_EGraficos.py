# Definimos la función para la búsqueda en profundidad
def dfs(graph, start, visited=None):
    # Si no se ha proporcionado un conjunto de nodos visitados, lo creamos
    if visited is None:
        visited = set()
    
    # Añadimos el nodo actual a los nodos visitados
    visited.add(start)
    
    # Imprimimos el nodo que estamos visitando
    print("Visitando nodo:", start)
    
    # Recorremos los nodos vecinos del nodo actual
    for neighbor in graph[start]:
        # Si el vecino no ha sido visitado
        if neighbor not in visited:
            # Llamamos recursivamente a la función DFS para el vecino
            dfs(graph, neighbor, visited)

# Grafo de ejemplo representado como un diccionario
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Nodo de inicio para la búsqueda
start_node = 'A'

# Llamamos a la función DFS con el grafo y el nodo de inicio
dfs(graph, start_node)

