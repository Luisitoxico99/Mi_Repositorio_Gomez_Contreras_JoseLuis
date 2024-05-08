class ForwardChecking:
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints

    def forward_checking(self, assignment):
        if len(assignment) == len(self.variables):
            return assignment

        var = self.select_unassigned_variable(assignment)
        for value in self.order_domain_values(var, assignment):
            if self.is_consistent(assignment.copy(), var, value):
                new_assignment = assignment.copy()
                new_assignment[var] = value

                # Realizar comprobación hacia adelante
                if self.forward_check(var, value, new_assignment):
                    result = self.forward_checking(new_assignment)
                    if result:
                        return result

        return None

    def forward_check(self, var, value, assignment):
        for neighbor in self.get_neighbors(var):
            if neighbor not in assignment:
                for neighbor_value in self.domains[neighbor][:]:
                    assignment[neighbor] = neighbor_value
                    if not self.is_consistent(assignment, neighbor, neighbor_value):
                        self.domains[neighbor].remove(neighbor_value)
                if not self.domains[neighbor]:
                    return False
        return True

    def select_unassigned_variable(self, assignment):
        for var in self.variables:
            if var not in assignment:
                return var
        return None

    def order_domain_values(self, var, assignment):
        return self.domains[var]

    def is_consistent(self, assignment, var, value):
        assignment[var] = value
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

forward_checking = ForwardChecking(variables, domains, constraints)
solution = forward_checking.forward_checking({})

if solution:
    print("Solución encontrada:")
    print(solution)
else:
    print("No se encontró una solución.")
