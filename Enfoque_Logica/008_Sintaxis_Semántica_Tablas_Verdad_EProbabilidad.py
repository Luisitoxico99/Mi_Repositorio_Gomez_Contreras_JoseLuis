import itertools

def tabla_verdad(expresion):
    variables = sorted(set(expresion.replace("(", "").replace(")", "").replace("¬", "").replace("&", "").replace("|", "").split()))
    encabezado = " | ".join(variables + [expresion])
    separador = "-" * len(encabezado)
    print(separador)
    print(encabezado)
    print(separador)

    for valores in itertools.product([True, False], repeat=len(variables)):
        asignacion = dict(zip(variables, valores))
        valores_verdad = [str(asignacion[var]) for var in variables]
        valores_verdad.append(str(eval(expresion, asignacion)))
        fila = " | ".join(valores_verdad)
        print(fila)

# Ejemplo de uso
expresion = "(p & q) | ¬r"
tabla_verdad(expresion)
