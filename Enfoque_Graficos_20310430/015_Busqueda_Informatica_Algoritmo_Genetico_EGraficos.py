import random

class GeneticAlgorithm:
    def __init__(self, population_size, gene_length, fitness_func, crossover_rate=0.8, mutation_rate=0.01):
        self.population_size = population_size
        self.gene_length = gene_length
        self.fitness_func = fitness_func
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate

    def generate_population(self):
        return [[random.randint(0, 1) for _ in range(self.gene_length)] for _ in range(self.population_size)]

    def selection(self, population):
        fitness_values = [self.fitness_func(individual) for individual in population]
        total_fitness = sum(fitness_values)
        probabilities = [fitness / total_fitness for fitness in fitness_values]
        return random.choices(population, weights=probabilities, k=2)

    def crossover(self, parent1, parent2):
        if random.random() < self.crossover_rate:
            crossover_point = random.randint(1, self.gene_length - 1)
            child1 = parent1[:crossover_point] + parent2[crossover_point:]
            child2 = parent2[:crossover_point] + parent1[crossover_point:]
            return child1, child2
        else:
            return parent1, parent2

    def mutation(self, individual):
        for i in range(self.gene_length):
            if random.random() < self.mutation_rate:
                individual[i] = 1 - individual[i]
        return individual

    def evolve(self, population):
        new_population = []

        while len(new_population) < self.population_size:
            parent1, parent2 = self.selection(population)
            child1, child2 = self.crossover(parent1, parent2)
            child1 = self.mutation(child1)
            child2 = self.mutation(child2)
            new_population.extend([child1, child2])

        return new_population

    def run(self, generations):
        population = self.generate_population()
        for _ in range(generations):
            population = self.evolve(population)
        
        # Seleccionar el mejor individuo de la población final
        best_individual = max(population, key=self.fitness_func)
        best_fitness = self.fitness_func(best_individual)
        return best_individual, best_fitness

# Ejemplo de una función de aptitud para maximizar el número de unos en una cadena binaria
def binary_fitness(individual):
    return sum(individual)

# Creamos una instancia del algoritmo genético y ejecutamos el algoritmo
population_size = 100
gene_length = 10
genetic_algorithm = GeneticAlgorithm(population_size, gene_length, binary_fitness)
best_individual, best_fitness = genetic_algorithm.run(generations=100)

# Imprimimos el mejor individuo encontrado y su aptitud
print("El mejor individuo encontrado es:", best_individual)
print("Su aptitud es:", best_fitness)
