class LogicaModal:
    def __init__(self, modelo):
        self.modelo = modelo

    def necesidad(self, proposicion):
        # Verifica si la proposición es necesaria en el modelo
        return proposicion in self.modelo

    def posibilidad(self, proposicion):
        # Verifica si la proposición es posible en el modelo
        return True  # Para un modelo simple, todas las proposiciones son posibles

# Ejemplo de uso
modelo = {"p", "q", "r"}  # Definimos un modelo con algunas proposiciones
logica = LogicaModal(modelo)

# Consultas modales
print("¿Es necesario que 'p' sea verdadero?", logica.necesidad("p"))
print("¿Es posible que 'r' sea verdadero?", logica.posibilidad("r"))
