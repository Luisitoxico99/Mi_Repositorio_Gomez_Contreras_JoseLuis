class ConflictDirectedBackjumping:
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints
        self.conflicts = {}  # Almacena el nivel de conflicto para cada variable

    def backjumping_search(self):
        return self.backjump({}, 0)

    def backjump(self, assignment, level):
        if len(assignment) == len(self.variables):
            return assignment

        var = self.select_unassigned_variable(assignment)
        for value in self.order_domain_values(var, assignment):
            if self.is_consistent(assignment.copy(), var, value):
                assignment[var] = value
                result = self.backjump(assignment, level)
                if result:
                    return result
                del assignment[var]

        # Salto atrás basado en el conflicto
        if level > 0:
            var_with_conflict = max(self.conflicts, key=self.conflicts.get)
            if var_with_conflict in assignment:
                del assignment[var_with_conflict]
            return self.backjump(assignment, level - 1)

        return None

    def is_consistent(self, assignment, var, value):
        assignment[var] = value
        for constraint in self.constraints:
            if not constraint(assignment):
                # Marcar conflicto
                self.conflicts[var] = len(assignment)
                return False
        return True

    def select_unassigned_variable(self, assignment):
        for var in self.variables:
            if var not in assignment:
                return var
        return None

    def order_domain_values(self, var, assignment):
        return self.domains[var]

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

cdbj = ConflictDirectedBackjumping(variables, domains, constraints)
solution = cdbj.backjumping_search()

if solution:
    print("Solución encontrada:")
    print(solution)
else:
    print("No se encontró una solución.")
