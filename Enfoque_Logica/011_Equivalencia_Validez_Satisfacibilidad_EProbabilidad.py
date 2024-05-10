from sympy import symbols, Equivalent

# Definimos las variables
p, q = symbols('p q')

# Expresiones a comparar
expresion1 = p & q
expresion2 = q & p

# Verificar equivalencia
equivalencia = Equivalent(expresion1, expresion2)
print("¿Las expresiones son equivalentes?", equivalencia)
