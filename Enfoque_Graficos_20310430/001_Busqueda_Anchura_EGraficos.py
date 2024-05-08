from collections import deque

# Definimos la función para la búsqueda en anchura
def bfs(graph, start):
    # Creamos una cola para almacenar los nodos a visitar
    queue = deque([start])
    
    # Creamos un conjunto para almacenar los nodos ya visitados
    visited = set([start])
    
    # Mientras la cola no esté vacía
    while queue:
        # Sacamos un nodo de la cola
        node = queue.popleft()
        
        # Imprimimos el nodo que estamos visitando
        print("Visitando nodo:", node)
        
        # Recorremos los nodos vecinos del nodo actual
        for neighbor in graph[node]:
            # Si el vecino no ha sido visitado
            if neighbor not in visited:
                # Lo marcamos como visitado
                visited.add(neighbor)
                
                # Lo agregamos a la cola para visitarlo luego
                queue.append(neighbor)

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

# Llamamos a la función BFS con el grafo y el nodo de inicio
bfs(graph, start_node)

