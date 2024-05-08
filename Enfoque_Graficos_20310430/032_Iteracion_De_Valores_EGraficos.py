# Definición de la clase para representar una red de decisión
class DecisionNetwork:
    def __init__(self):
        self.nodes = {}  # Diccionario para almacenar los nodos de la red de decisión y sus valores

    def add_node(self, node_name, values):
        self.nodes[node_name] = values  # Agregar nodo con sus valores

    def value_iteration(self, max_iterations=100, convergence_threshold=0.01):
        # Inicializar los valores de los nodos a cero
        for values in self.nodes.values():
            for key in values:
                values[key] = 0

        # Iterar hasta que se alcance la convergencia o se llegue al número máximo de iteraciones
        for iteration in range(max_iterations):
            delta = 0  # Inicializar el cambio máximo de valor en esta iteración
            for node_name, values in self.nodes.items():
                # Calcular el nuevo valor del nodo como el máximo de las utilidades esperadas
                new_value = max(self.calculate_expected_utilities(node_name))
                # Calcular el cambio máximo de valor en esta iteración
                delta = max(delta, abs(new_value - values['current']))
                # Actualizar el valor del nodo
                values['current'] = new_value
            # Verificar la convergencia
            if delta < convergence_threshold:
                break

    def calculate_expected_utilities(self, node_name):
        # Calcular las utilidades esperadas para cada posible valor del nodo
        expected_utilities = []
        for value, utility in self.nodes[node_name]['utilities'].items():
            expected_utility = utility  # Utilidad propia del valor del nodo
            for parent_name, parent_value in self.nodes[node_name]['parents'].items():
                # Multiplicar la utilidad del padre por la probabilidad del valor del padre
                expected_utility += parent_value * self.nodes[parent_name][value]['current']
            expected_utilities.append(expected_utility)
        return expected_utilities

    def print_values(self):
        print("Valores finales de los nodos:")
        for node_name, values in self.nodes.items():
            print(f"{node_name}: {values['current']}")

# Ejemplo de uso
if __name__ == "__main__":
    # Crear una red de decisión con nodos y valores
    network = DecisionNetwork()
    network.add_node('Lluvia', {
        'Sí': {'current': 0, 'parents': {}, 'utilities': {'Sí': 0.2, 'No': 0.8}},
        'No': {'current': 0, 'parents': {}, 'utilities': {'Sí': 0.8, 'No': 0.2}}
    })
    network.add_node('Tráfico', {
        'Sí': {'current': 0, 'parents': {'Lluvia': 0.6}, 'utilities': {'Sí': 0.6, 'No': 0.4}},
        'No': {'current': 0, 'parents': {'Lluvia': 0.4}, 'utilities': {'Sí': 0.4, 'No': 0.6}}
    })
    network.add_node('Llegar_Tarde', {
        'Sí': {'current': 0, 'parents': {'Lluvia': 0.9, 'Tráfico': 0.7}, 'utilities': {'Sí': 0.9, 'No': 0.1}},
        'No': {'current': 0, 'parents': {'Lluvia': 0.1, 'Tráfico': 0.3}, 'utilities': {'Sí': 0.1, 'No': 0.9}}
    })

    # Ejecutar la iteración de valores
    network.value_iteration()

    # Imprimir los valores finales de los nodos
    network.print_values()
