import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo dirigido para representar la red de decisión
G = nx.DiGraph()

# Definir nodos y aristas
nodes = ['Lluvia', 'Tráfico', 'Llegar_Tarde']
edges = [('Lluvia', 'Llegar_Tarde'), ('Tráfico', 'Llegar_Tarde')]

# Agregar nodos al grafo
G.add_nodes_from(nodes)

# Agregar aristas al grafo
G.add_edges_from(edges)

# Asignar probabilidad condicional a cada nodo
probabilities = {
    'Lluvia': 0.2,        # Probabilidad de lluvia
    'Tráfico': {          # Probabilidad de tráfico condicionada a la lluvia
        'Lluvia': 0.8,
        '~Lluvia': 0.4
    },
    'Llegar_Tarde': {     # Probabilidad de llegar tarde condicionada al tráfico y la lluvia
        ('Lluvia', 'Tráfico'): {  # Caso: Lluvia y Tráfico
            'Llegar_Tarde': 0.9,
            '~Llegar_Tarde': 0.1
        },
        ('Lluvia', '~Tráfico'): {  # Caso: Lluvia y No Tráfico
            'Llegar_Tarde': 0.6,
            '~Llegar_Tarde': 0.4
        },
        ('~Lluvia', 'Tráfico'): {  # Caso: No Lluvia y Tráfico
            'Llegar_Tarde': 0.7,
            '~Llegar_Tarde': 0.3
        },
        ('~Lluvia', '~Tráfico'): {  # Caso: No Lluvia y No Tráfico
            'Llegar_Tarde': 0.3,
            '~Llegar_Tarde': 0.7
        }
    }
}

# Agregar atributos de probabilidad a los nodos
for node, prob in probabilities.items():
    G.nodes[node]['probability'] = prob

# Agregar atributos de probabilidad a las aristas
for u, v, prob in probabilities['Llegar_Tarde'].items():
    G[u][v]['probability'] = prob

# Dibujar el grafo
pos = nx.spring_layout(G)  # Calcular posiciones de los nodos
nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightblue', font_size=12, font_weight='bold', arrowsize=20)
labels = nx.get_edge_attributes(G, 'probability')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Red de Decisión: Lluvia -> Tráfico -> Llegar_Tarde")
plt.show()
