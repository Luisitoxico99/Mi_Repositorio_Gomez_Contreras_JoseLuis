import numpy as np

class DecisionNetwork:
    def __init__(self):
        self.nodes = {}  # Diccionario para almacenar los nodos de la red de decisión y sus valores
        self.discount_factor = 0.9  # Factor de descuento para las utilidades futuras

    def add_node(self, node_name, values):
        self.nodes[node_name] = values  # Agregar nodo con sus valores

    def policy_iteration(self, max_iterations=100):
        # Inicializar la política aleatoria
        policy = {node_name: np.random.choice(list(values['utilities'].keys())) for node_name, values in self.nodes.items()}

        # Iterar hasta que se alcance el número máximo de iteraciones
        for _ in range(max_iterations):
            # Evaluar la política actual
            values = self.evaluate_policy(policy)
            # Mejorar la política
            new_policy = self.improve_policy(values)
            # Si la política no cambia, terminar
            if new_policy == policy:
                break
            policy = new_policy

        return policy

    def evaluate_policy(self, policy):
        # Inicializar los valores de los nodos a cero
        for values in self.nodes.values():
            values['current'] = 0

        # Iterar hasta que se alcance la convergencia
        while True:
            delta = 0
            for node_name, values in self.nodes.items():
                # Calcular la utilidad esperada para el valor de la política actual
                new_value = values['utilities'][policy[node_name]] + self.discount_factor * sum(
                    values['parents'][parent_name] * self.nodes[parent_name]['current'] for parent_name in values['parents'])
                delta = max(delta, abs(new_value - values['current']))
                values['current'] = new_value
            if delta < 0.01:
                break

        return {node_name: values['current'] for node_name, values in self.nodes.items()}

    def improve_policy(self, values):
        # Mejorar la política basada en los nuevos valores
        new_policy = {}
        for node_name, values in self.nodes.items():
            # Elegir el valor que maximice la utilidad esperada
            new_policy[node_name] = max(values['utilities'], key=lambda x: values['utilities'][x] +
                                        self.discount_factor * sum(values['parents'][parent_name] * values['current']
                                                                   for parent_name in values['parents']))
        return new_policy


# Ejemplo de uso
if __name__ == "__main__":
    # Crear una red de decisión con nodos y valores
    network = DecisionNetwork()
    network.add_node('Lluvia', {
        'utilities': {'Sí': 0.2, 'No': 0.8},
        'parents': {}
    })
    network.add_node('Tráfico', {
        'utilities': {'Sí': 0.6, 'No': 0.4},
        'parents': {'Lluvia': 0.6}
    })
    network.add_node('Llegar_Tarde', {
        'utilities': {'Sí': 0.9, 'No': 0.1},
        'parents': {'Lluvia': 0.9, 'Tráfico': 0.7}
    })

    # Ejecutar la iteración de políticas
    policy = network.policy_iteration()

    # Imprimir la política resultante
    print("Política resultante:")
    for node_name, value in policy.items():
        print(f"{node_name}: {value}")
