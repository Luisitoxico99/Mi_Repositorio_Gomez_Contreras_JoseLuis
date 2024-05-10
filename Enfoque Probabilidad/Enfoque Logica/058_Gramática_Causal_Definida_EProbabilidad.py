import re

class AnalizadorSintactico:
    def __init__(self, cadena):
        self.cadena = cadena
        self.posicion_actual = 0

    def analizar(self):
        try:
            arbol_sintaxis = self.expresion()
            # Verificar si se llegó al final de la cadena
            if self.posicion_actual != len(self.cadena):
                raise Exception("Error: Cadena no completamente analizada.")
            print("El análisis sintáctico se completó con éxito.")
            return arbol_sintaxis
        except Exception as e:
            print("Error de sintaxis:", e)

    # Reglas de la gramática
    def expresion(self):
        termino = self.termino()
        while self.posicion_actual < len(self.cadena) and self.cadena[self.posicion_actual] in ['+', '-']:
            operador = self.consumir('+') if self.cadena[self.posicion_actual] == '+' else self.consumir('-')
            expresion_derecha = self.termino()
            termino = {'Tipo': 'Operacion', 'Operador': operador, 'Izquierda': termino, 'Derecha': expresion_derecha}
        return termino

    def termino(self):
        factor = self.factor()
        while self.posicion_actual < len(self.cadena) and self.cadena[self.posicion_actual] in ['*', '/']:
            operador = self.consumir('*') if self.cadena[self.posicion_actual] == '*' else self.consumir('/')
            termino_derecho = self.factor()
            factor = {'Tipo': 'Operacion', 'Operador': operador, 'Izquierda': factor, 'Derecha': termino_derecho}
        return factor

    def factor(self):
        if self.cadena[self.posicion_actual].isdigit():
            return {'Tipo': 'Numero', 'Valor': self.consumir_numero()}
        elif self.cadena[self.posicion_actual] == '(':
            self.consumir('(')
            expresion_interna = self.expresion()
            self.consumir(')')
            return expresion_interna
        else:
            raise Exception("Factor no reconocido.")

    # Métodos auxiliares
    def consumir(self, token_esperado):
        if self.posicion_actual < len(self.cadena) and self.cadena[self.posicion_actual] == token_esperado:
            self.posicion_actual += 1
            return token_esperado
        else:
            raise Exception(f"Se esperaba '{token_esperado}', pero se encontró '{self.cadena[self.posicion_actual]}' en la posición {self.posicion_actual}.")

    def consumir_numero(self):
        numero = ''
        while self.posicion_actual < len(self.cadena) and self.cadena[self.posicion_actual].isdigit():
            numero += self.cadena[self.posicion_actual]
            self.posicion_actual += 1
        return int(numero)

# Ejemplo de uso
cadena = "2 + 3 * (4 - 1)"
analizador = AnalizadorSintactico(cadena)
arbol_sintaxis = analizador.analizar()
print("Árbol de sintaxis:", arbol_sintaxis)
