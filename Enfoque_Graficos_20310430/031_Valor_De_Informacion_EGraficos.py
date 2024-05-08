# Definición de la clase para representar una red de decisión
class DecisionNetwork:
    def __init__(self):
        self.nodes = {}  # Diccionario para almacenar los nodos de la red de decisión y sus probabilidades

    def add_node(self, node_name, probabilities):
        self.nodes[node_name] = probabilities  # Agregar nodo con sus probabilidades

    def value_of_information(self, uncertain_variable):
        # Calcular la utilidad esperada antes de conocer la información
        initial_expected_utility = self.expected_utility()

        # Calcular la utilidad esperada después de conocer la información
        updated_expected_utility = 0
        for value, probability in self.nodes[uncertain_variable].items():
            # Actualizar la probabilidad del nodo de la variable incierta
            self.nodes[uncertain_variable] = {value: probability}
            # Calcular la nueva utilidad esperada
            updated_expected_utility += probability * self.expected_utility()

        # Calcular el valor de la información como la diferencia en la utilidad esperada
        value_of_information = updated_expected_utility - initial_expected_utility
        return value_of_information

    def expected_utility(self):
        # Simplemente como ejemplo, asumimos que la utilidad esperada es la suma de las utilidades ponderadas por las probabilidades
        expected_utility = sum(prob * utility for prob, utility in self.calculate_outcome_probabilities())
        return expected_utility

    def calculate_outcome_probabilities(self):
        # Calcular las probabilidades de los resultados posibles
        outcome_probabilities = []
        for values in zip(*self.nodes.values()):
            probability = 1
            for prob in values:
                probability *= prob
            outcome_probabilities.append(probability)
        return outcome_probabilities

# Ejemplo de uso
if __name__ == "__main__":
    # Crear una red de decisión con nodos y probabilidades
    network = DecisionNetwork()
    network.add_node('Lluvia', {'Sí': 0.2, 'No': 0.8})
    network.add_node('Tráfico', {'Sí': 0.6, 'No': 0.4})
    network.add_node('Llegar_Tarde', {
        ('Sí', 'Sí'): 0.9, ('Sí', 'No'): 0.6,
        ('No', 'Sí'): 0.7, ('No', 'No'): 0.3
    })

    # Calcular el valor de la información de la variable 'Lluvia'
    voi = network.value_of_information('Lluvia')

    # Imprimir el valor de la información
    print("El valor de la información de la variable 'Lluvia' es:", voi)
