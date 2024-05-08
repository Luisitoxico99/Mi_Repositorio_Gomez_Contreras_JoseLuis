import random

class LocalBeamSearch:
    def __init__(self, initial_solutions, evaluate_func, neighbors_func, beam_width=5, max_iterations=100):
        self.current_solutions = initial_solutions
        self.evaluate_func = evaluate_func
        self.neighbors_func = neighbors_func
        self.beam_width = beam_width
        self.max_iterations = max_iterations

    def search(self):
        for _ in range(self.max_iterations):
            # Generar vecinos para todas las soluciones actuales
            all_neighbors = []
            for solution in self.current_solutions:
                all_neighbors.extend(self.neighbors_func(solution))

            # Evaluar todas las soluciones vecinas
            evaluated_neighbors = [(neighbor, self.evaluate_func(neighbor)) for neighbor in all_neighbors]

            # Seleccionar las mejores soluciones según el beam_width
            sorted_neighbors = sorted(evaluated_neighbors, key=lambda x: x[1])
            selected_neighbors = [neighbor for neighbor, _ in sorted_neighbors[:self.beam_width]]

            # Actualizar las soluciones actuales con las mejores vecinas seleccionadas
            self.current_solutions = selected_neighbors

        # Devolver la mejor solución encontrada
        best_solution = min(self.current_solutions, key=self.evaluate_func)
        return best_solution, self.evaluate_func(best_solution)

# Ejemplo de una función de evaluación simple para un problema unidimensional
def simple_evaluate(solution):
    return -solution ** 2  # Minimizar la función cuadrática

# Ejemplo de una función para generar vecinos en un problema unidimensional
def simple_neighbors(solution):
    return [solution + 1, solution - 1]

# Creamos instancias de soluciones iniciales y ejecutamos la búsqueda de Haz Local
initial_solutions = [0, 1, 2, 3, 4]  # Soluciones iniciales
local_beam_search = LocalBeamSearch(initial_solutions, simple_evaluate, simple_neighbors)
best_solution, best_score = local_beam_search.search()

# Imprimimos la mejor solución encontrada
print("La mejor solución encontrada es:", best_solution)
print("El mejor puntaje encontrado es:", best_score)
