import random

class TabuSearch:
    def __init__(self, initial_solution, neighbors_func, evaluate_func, tabu_tenure=5, max_iterations=100):
        self.current_solution = initial_solution
        self.tabu_list = []
        self.tabu_tenure = tabu_tenure
        self.max_iterations = max_iterations
        self.neighbors_func = neighbors_func
        self.evaluate_func = evaluate_func

    def search(self):
        iteration = 0
        best_solution = self.current_solution
        best_score = self.evaluate_func(best_solution)

        while iteration < self.max_iterations:
            neighbors = self.neighbors_func(self.current_solution)

            # Selecciona el mejor vecino que no esté en la lista tabú
            best_neighbor = min(neighbors, key=lambda x: self.evaluate_func(x) if x not in self.tabu_list else float('inf'))

            # Actualiza la lista tabú
            self.tabu_list.append(best_neighbor)
            if len(self.tabu_list) > self.tabu_tenure:
                self.tabu_list.pop(0)

            # Mueve a la mejor solución vecina
            self.current_solution = best_neighbor

            # Actualiza la mejor solución encontrada hasta ahora
            current_score = self.evaluate_func(self.current_solution)
            if current_score < best_score:
                best_solution = self.current_solution
                best_score = current_score

            iteration += 1

        return best_solution, best_score

# Función de vecinos simple para un problema de optimización unidimensional
def simple_neighbors(solution):
    return [solution + 1, solution - 1]

# Función de evaluación para el mismo problema unidimensional
def simple_evaluate(solution):
    return -solution ** 2  # Minimizar la función cuadrática

# Creamos una instancia de búsqueda tabú y ejecutamos la búsqueda
initial_solution = 0  # Estado inicial
tabu_search = TabuSearch(initial_solution, simple_neighbors, simple_evaluate)
best_solution, best_score = tabu_search.search()

# Imprimimos la mejor solución encontrada
print("La mejor solución encontrada es:", best_solution)
print("El mejor puntaje encontrado es:", best_score)
