from sympy import symbols, ForAll, Exists

# Definimos las variables
x = symbols('x')

# Expresión con cuantificadores
expresion_universal = ForAll(x, x**2 >= 0)
expresion_existencial = Exists(x, x**2 == 4)

# Mostramos las expresiones
print("Expresión con cuantificador universal:", expresion_universal)
print("Expresión con cuantificador existencial:", expresion_existencial)

# Evaluamos las expresiones
print("¿La expresión con cuantificador universal es verdadera?", expresion_universal)
print("¿La expresión con cuantificador existencial es verdadera?", expresion_existencial)
