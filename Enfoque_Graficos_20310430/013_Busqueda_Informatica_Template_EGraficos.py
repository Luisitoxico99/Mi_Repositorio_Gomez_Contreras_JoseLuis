import math
import random

class SimulatedAnnealing:
    def __init__(self, initial_solution, evaluate_func, neighbors_func, initial_temperature=100, cooling_rate=0.95, min_temperature=0.001):
        self.current_solution = initial_solution
        self.best_solution = initial_solution
        self.evaluate_func = evaluate_func
        self.neighbors_func = neighbors_func
        self.temperature = initial_temperature
        self.cooling_rate = cooling_rate
        self.min_temperature = min_temperature

    def search(self, max_iterations):
        for iteration in range(max_iterations):
            if self.temperature < self.min_temperature:
                break
            
            # Generar una solución vecina aleatoria
            neighbor_solution = random.choice(self.neighbors_func(self.current_solution))
            
            # Calcular la diferencia de energía entre la solución actual y la vecina
            energy_diff = self.evaluate_func(neighbor_solution) - self.evaluate_func(self.current_solution)
            
            # Si la nueva solución es mejor o se acepta peores soluciones según la probabilidad de Boltzmann
            if energy_diff < 0 or random.random() < math.exp(-energy_diff / self.temperature):
                self.current_solution = neighbor_solution
                
                # Actualizar la mejor solución encontrada hasta ahora
                if self.evaluate_func(neighbor_solution) < self.evaluate_func(self.best_solution):
                    self.best_solution = neighbor_solution
            
            # Enfriar la temperatura
            self.temperature *= self.cooling_rate

        return self.best_solution, self.evaluate_func(self.best_solution)

# Ejemplo de una función de evaluación simple para un problema unidimensional
def simple_evaluate(solution):
    return -solution ** 2  # Minimizar la función cuadrática

# Ejemplo de una función para generar vecinos en un problema unidimensional
