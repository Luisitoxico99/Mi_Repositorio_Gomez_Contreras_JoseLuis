class AnalizadorSintactico:
    def __init__(self, tokens):
        self.tokens = tokens
        self.posicion_actual = 0

    def analizar(self):
        try:
            arbol_sintaxis = self.programa()
            return arbol_sintaxis
        except Exception as e:
            print("Error de sintaxis:", e)

    # Reglas de la gramática
    def programa(self):
        return self.declaracion_variable()

    def declaracion_variable(self):
        tipo = self.consumir('TIPO')
        identificador = self.consumir('IDENTIFICADOR')
        self.consumir('ASIGNACION')
        valor = self.consumir('VALOR')
        self.consumir('PUNTO_COMA')
        return {'Tipo': tipo, 'Identificador': identificador, 'Valor': valor}

    # Métodos auxiliares
    def consumir(self, tipo_token):
        token_actual = self.tokens[self.posicion_actual]
        if token_actual[0] == tipo_token:
            self.posicion_actual += 1
            return token_actual[1]
        else:
            raise Exception(f"Se esperaba un token de tipo {tipo_token}, pero se encontró {token_actual[0]}")

# Ejemplo de uso
tokens = [('TIPO', 'int'), ('IDENTIFICADOR', 'x'), ('ASIGNACION', '='), ('VALOR', '10'), ('PUNTO_COMA', ';')]
parser = AnalizadorSintactico(tokens)
arbol_sintaxis = parser.analizar()
print("Árbol de Sintaxis:", arbol_sintaxis)
