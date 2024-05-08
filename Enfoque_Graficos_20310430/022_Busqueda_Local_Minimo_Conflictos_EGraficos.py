import random

class MinConflicts:
    def __init__(self, variables, domains, constraints, max_steps=1000):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints
        self.max_steps = max_steps

    def initial_assignment(self):
        assignment = {}
        for var in self.variables:
            assignment[var] = random.choice(self.domains[var])
        return assignment

    def min_conflicts_search(self):
        current_assignment = self.initial_assignment()
        for _ in range(self.max_steps):
            if self.is_solution(current_assignment):
                return current_assignment
            var = self.select_conflicted_variable(current_assignment)
            value = self.select_best_value(var, current_assignment)
            current_assignment[var] = value
        return None

    def select_conflicted_variable(self, assignment):
        conflicted_variables = [var for var in assignment if not self.is_consistent(assignment, var)]
        return random.choice(conflicted_variables)

    def select_best_value(self, var, assignment):
        min_conflicts = float('inf')
        best_value = None
        for value in self.domains[var]:
            assignment[var] = value
            conflicts = sum(not self.is_consistent(assignment, neighbor) for neighbor in self.get_neighbors(var))
            if conflicts < min_conflicts:
                min_conflicts = conflicts
                best_value = value
        return best_value

    def is_solution(self, assignment):
        return all(self.is_consistent(assignment, var) for var in assignment)

    def is_consistent(self, assignment, var):
        for neighbor in self.get_neighbors(var):
            if neighbor in assignment and not self.constraint_satisfied(var, assignment[var], neighbor, assignment[neighbor]):
                return False
        return True

    def get_neighbors(self, var):
        neighbors = []
        for constraint in self.constraints:
            if var in constraint.__code__.co_varnames:
                neighbors.extend([v for v in constraint.__code__.co_varnames if v != var])
        return neighbors

    def constraint_satisfied(self, var_i, value_i, var_j, value_j):
        for constraint in self.constraints:
            if var_i in constraint.__code__.co_varnames and var_j in constraint.__code__.co_varnames:
                if not constraint({var_i: value_i, var_j: value_j}):
                    return False
        return True

# Ejemplo de uso
variables = ['A', 'B', 'C']
domains = {
    'A': [1, 2],
    'B': [1, 2, 3],
    'C': [2, 3]
}

# Ejemplo de restricciones: A y B no pueden tener el mismo valor
def constraint_AB(assignment):
    return assignment.get('A') != assignment.get('B')

# Ejemplo de restricciones: C debe ser mayor que A y B
def constraint_C_greater_than_A_and_B(assignment):
    return assignment.get('C') > assignment.get('A') and assignment.get('C') > assignment.get('B')

constraints = [constraint_AB, constraint_C_greater_than_A_and_B]

min_conflicts = MinConflicts(variables, domains, constraints)
solution = min_conflicts.min_conflicts_search()

if solution:
    print("Solución encontrada:")
    print(solution)
else:
    print("No se encontró una solución.")
