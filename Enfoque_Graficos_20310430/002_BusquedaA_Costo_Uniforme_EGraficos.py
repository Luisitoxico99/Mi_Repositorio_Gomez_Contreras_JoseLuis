import heapq

# Definimos la función para la búsqueda en anchura de costo uniforme
def ucs(graph, start, goal):
    # Creamos una cola de prioridad para almacenar los nodos a visitar
    queue = [(0, start)]  # (costo, nodo)
    
    # Creamos un diccionario para almacenar los costos mínimos conocidos
    cost_so_far = {start: 0}
    
    # Mientras la cola de prioridad no esté vacía
    while queue:
        # Sacamos el nodo con menor costo de la cola de prioridad
        current_cost, current_node = heapq.heappop(queue)
        
        # Si hemos llegado al nodo objetivo, terminamos
        if current_node == goal:
            break
        
        # Recorremos los nodos vecinos del nodo actual
        for next_node, cost in graph[current_node].items():
            # Calculamos el costo total para llegar al vecino a través del nodo actual
            new_cost = current_cost + cost
            
            # Si es la primera vez que visitamos el vecino o encontramos un costo menor
            if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                # Actualizamos el costo mínimo conocido para el vecino
                cost_so_far[next_node] = new_cost
                
                # Agregamos el vecino a la cola de prioridad con su nuevo costo
                heapq.heappush(queue, (new_cost, next_node))
    
    # Devolvemos el costo mínimo para llegar al nodo objetivo
    return cost_so_far.get(goal, float('inf'))

# Grafo de ejemplo representado como un diccionario de diccionarios
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'D': 5},
    'C': {'A': 2, 'D': 8},
    'D': {'B': 5, 'C': 8}
}

# Nodo de inicio y nodo objetivo para la búsqueda
start_node = 'A'
goal_node = 'D'

# Llamamos a la función UCS con el grafo, el nodo de inicio y el nodo objetivo
minimum_cost = ucs(graph, start_node, goal_node)

print("El costo mínimo desde", start_node, "a", goal_node, "es:", minimum_cost)

