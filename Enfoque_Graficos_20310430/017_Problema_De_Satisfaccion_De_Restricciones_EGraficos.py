class CSP:
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints

    def is_consistent(self, assignment):
        for constraint in self.constraints:
            if not constraint(assignment):
                return False
        return True

    def backtracking_search(self):
        return self.backtrack({}, self.variables)

    def backtrack(self, assignment, remaining_variables):
        if not remaining_variables:
            return assignment

        var = remaining_variables[0]
        for value in self.domains[var]:
            new_assignment = assignment.copy()
            new_assignment[var] = value
            if self.is_consistent(new_assignment):
                result = self.backtrack(new_assignment, remaining_variables[1:])
                if result is not None:
                    return result
        return None

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

csp = CSP(variables, domains, constraints)
solution = csp.backtracking_search()

if solution:
    print("Solución encontrada:")
    print(solution)
else:
    print("No se encontró una solución.")
