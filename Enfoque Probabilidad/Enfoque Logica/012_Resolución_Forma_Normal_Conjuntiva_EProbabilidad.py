from sympy import to_cnf

# Expresión a convertir
expresion = Or(Or(p, q), Or(Not(p), q))

# Convertir a FNC
fnc = to_cnf(expresion)
print("Forma Normal Conjuntiva:", fnc)
