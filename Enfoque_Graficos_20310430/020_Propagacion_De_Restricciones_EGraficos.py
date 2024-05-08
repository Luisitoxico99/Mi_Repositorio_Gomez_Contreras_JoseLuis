class ConstraintPropagation:
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints

    def ac3(self):
        queue = self.initial_queue()

        while queue:
            (var_i, var_j) = queue.pop(0)
            if self.revise(var_i, var_j):
                if len(self.domains[var_i]) == 0:
                    return False
                for var_k in self.get_neighbors(var_i):
                    if var_k != var_j:
                        queue.append((var_k, var_i))

        return True

    def revise(self, var_i, var_j):
        revised = False
        for value_i in self.domains[var_i][:]:
            if not any(self.is_consistent({var_i: value_i, var_j: value_j}) for value_j in self.domains[var_j]):
                self.domains[var_i].remove(value_i)
                revised = True
        return revised

    def initial_queue(self):
        queue = []
        for constraint in self.constraints:
            (var_i, var_j) = self.get_constraint_vars(constraint)
            queue.append((var_i, var_j))
        return queue

    def is_consistent(self, assignment):
        for constraint in self.constraints:
            if not constraint(assignment):
                return False
        return True

    def get_neighbors(self, var):
        neighbors = []
        for constraint in self.constraints:
            if var in constraint.__code__.co_varnames:
                neighbors.extend([v for v in constraint.__code__.co_varnames if v != var])
        return neighbors

    def get_constraint_vars(self, constraint):
        return constraint.__code__.co_varnames[:2]

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

propagation = ConstraintPropagation(variables, domains, constraints)
result = propagation.ac3()

if result:
    print("Restricciones consistentes después de la propagación.")
else:
    print("No se encontró una solución consistente.")
