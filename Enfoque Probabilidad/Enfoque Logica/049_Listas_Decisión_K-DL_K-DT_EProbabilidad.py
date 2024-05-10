class DecisionList:
    def __init__(self, reglas):
        self.reglas = reglas
    
    def predecir(self, instancia):
        for condicion, decision in self.reglas:
            if condicion(instancia):
                return decision
        return None

# Ejemplo de uso
# Supongamos que tenemos un conjunto de datos con dos características: x1 y x2
# Y queremos clasificar las instancias en dos clases: 0 o 1

# Definimos algunas reglas de decisión
reglas = [
    (lambda x: x[0] < 0.5 and x[1] < 0.5, 0),
    (lambda x: x[0] >= 0.5 or x[1] >= 0.5, 1)
]

# Creamos la lista de decisiones
decision_list = DecisionList(reglas)

# Realizamos predicciones para algunas instancias
instancia_1 = [0.2, 0.3]
instancia_2 = [0.7, 0.8]
print("Predicción para la instancia 1:", decision_list.predecir(instancia_1))
print("Predicción para la instancia 2:", decision_list.predecir(instancia_2))
