# Definimos la función para la búsqueda bidireccional
def bidirectional_search(graph, start, goal):
    # Inicializamos dos conjuntos de nodos visitados, uno para cada dirección de búsqueda
    visited_forward = {start}
    visited_backward = {goal}
    
    # Inicializamos dos colas, una para cada dirección de búsqueda
    queue_forward = [start]
    queue_backward = [goal]
    
    # Mientras ambas colas no estén vacías
    while queue_forward and queue_backward:
        # Realizamos la búsqueda hacia adelante desde la cola forward
        node_forward = queue_forward.pop(0)
        
        # Imprimimos el nodo que estamos visitando en la búsqueda hacia adelante
        print("Visitando nodo hacia adelante:", node_forward)
        
        # Si encontramos una intersección entre las búsquedas hacia adelante y hacia atrás, hemos terminado
        if node_forward in visited_backward:
            print("¡Intersección encontrada en el nodo:", node_forward, "!")
            return True
        
        # Expandimos los nodos vecinos del nodo actual en la búsqueda hacia adelante
        for neighbor in graph[node_forward]:
            if neighbor not in visited_forward:
                visited_forward.add(neighbor)
                queue_forward.append(neighbor)
        
        # Realizamos la búsqueda hacia atrás desde la cola backward
        node_backward = queue_backward.pop(0)
        
        # Imprimimos el nodo que estamos visitando en la búsqueda hacia atrás
        print("Visitando nodo hacia atrás:", node_backward)
        
        # Si encontramos una intersección entre las búsquedas hacia adelante y hacia atrás, hemos terminado
        if node_backward in visited_forward:
            print("¡Intersección encontrada en el nodo:", node_backward, "!")
            return True
        
        # Expandimos los nodos vecinos del nodo actual en la búsqueda hacia atrás
        for neighbor in graph[node_backward]:
            if neighbor not in visited_backward:
                visited_backward.add(neighbor)
                queue_backward.append(neighbor)
    
    # Si no encontramos una intersección, la búsqueda no tuvo éxito
    print("No se encontró intersección.")
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

# Nodo de inicio y nodo objetivo para la búsqueda bidireccional
start_node = 'A'
goal_node = 'F'

# Llamamos a la función de búsqueda bidireccional con el grafo, el nodo de inicio y el nodo objetivo
result = bidirectional_search(graph, start_node, goal_node)

# Imprimimos el resultado de la búsqueda
if result:
    print("¡Se encontró un camino entre", start_node, "y", goal_node, "!")
else:
    print("No se encontró un camino entre", start_node, "y", goal_node, ".")

