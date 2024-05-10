import re

class AnalizadorLexico:
    def __init__(self, codigo_fuente):
        self.codigo_fuente = codigo_fuente
        self.posicion_actual = 0
        self.tokens = []

    def analizar(self):
        while self.posicion_actual < len(self.codigo_fuente):
            token = self.obtener_siguiente_token()
            if token:
                self.tokens.append(token)
            else:
                print("Error: Caracter no reconocido en la posición", self.posicion_actual)
                break
        return self.tokens

    def obtener_siguiente_token(self):
        # Expresiones regulares para reconocer diferentes tokens
        patron_identificador = r'[a-zA-Z][a-zA-Z0-9_]*'
        patron_numero = r'\d+'
        patron_operador = r'[+\-*/]'

        # Ignorar espacios en blanco
        if self.codigo_fuente[self.posicion_actual].isspace():
            self.posicion_actual += 1
            return None

        # Identificar identificadores
        if re.match(patron_identificador, self.codigo_fuente[self.posicion_actual:]):
            match = re.match(patron_identificador, self.codigo_fuente[self.posicion_actual:])
            token = match.group(0)
            self.posicion_actual += len(token)
            return ('IDENTIFICADOR', token)

        # Identificar números
        elif re.match(patron_numero, self.codigo_fuente[self.posicion_actual:]):
            match = re.match(patron_numero, self.codigo_fuente[self.posicion_actual:])
            token = match.group(0)
            self.posicion_actual += len(token)
            return ('NUMERO', token)

        # Identificar operadores
        elif re.match(patron_operador, self.codigo_fuente[self.posicion_actual]):
            token = self.codigo_fuente[self.posicion_actual]
            self.posicion_actual += 1
            return ('OPERADOR', token)

        # Caracter no reconocido
        else:
            return None

# Ejemplo de uso
codigo_fuente = "var x = 10 + y * 5;"
analizador = AnalizadorLexico(codigo_fuente)
tokens = analizador.analizar()
print("Tokens encontrados:", tokens)
