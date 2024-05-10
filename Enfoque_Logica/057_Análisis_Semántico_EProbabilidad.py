class AnalizadorSemantico:
    def __init__(self, arbol_sintaxis):
        self.arbol_sintaxis = arbol_sintaxis

    def analizar(self):
        try:
            self.validar_programa(self.arbol_sintaxis)
            print("El análisis semántico se completó sin errores.")
        except Exception as e:
            print("Error semántico:", e)

    def validar_programa(self, arbol):
        for nodo in arbol:
            if nodo['Tipo'] == 'DECLARACION_VARIABLE':
                self.validar_declaracion_variable(nodo)

    def validar_declaracion_variable(self, nodo):
        # Verificar si el tipo de la variable es válido
        tipo_variable = nodo['Tipo']
        if tipo_variable not in ['int', 'float', 'string']:
            raise Exception(f"Tipo de variable '{tipo_variable}' no válido.")

        # Verificar si el valor asignado es del mismo tipo que la variable
        valor_variable = nodo['Valor']
        if not isinstance(valor_variable, self.get_tipo_python(tipo_variable)):
            raise Exception("El tipo de la variable y el valor asignado no coinciden.")

    def get_tipo_python(self, tipo):
        # Mapeo de tipos del lenguaje a tipos de Python
        if tipo == 'int':
            return int
        elif tipo == 'float':
            return float
        elif tipo == 'string':
            return str

# Ejemplo de uso
arbol_sintaxis = [
    {'Tipo': 'DECLARACION_VARIABLE', 'Tipo': 'int', 'Identificador': 'x', 'Valor': 10},
    {'Tipo': 'DECLARACION_VARIABLE', 'Tipo': 'float', 'Identificador': 'y', 'Valor': 10.5},
    {'Tipo': 'DECLARACION_VARIABLE', 'Tipo': 'string', 'Identificador': 'z', 'Valor': 'hola'},
]
analizador = AnalizadorSemantico(arbol_sintaxis)
analizador.analizar()
