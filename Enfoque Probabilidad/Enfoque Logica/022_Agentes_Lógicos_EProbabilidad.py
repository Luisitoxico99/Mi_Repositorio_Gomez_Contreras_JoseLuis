class AgenteLogico:
    def __init__(self, base_conocimiento):
        self.base_conocimiento = base_conocimiento

    def realizar_inferencia(self, consulta):
        # Realiza inferencia lógica utilizando la base de conocimiento
        # Aquí podrías utilizar un motor de inferencia más sofisticado
        # Por simplicidad, en este ejemplo, solo se busca la consulta directamente en la base de conocimiento
        if consulta in self.base_conocimiento:
            return True
        else:
            return False

# Base de conocimiento inicial del agente
base_conocimiento = {"lluvia", "sol", "nublado", "viento"}

# Crear una instancia del agente lógico
agente = AgenteLogico(base_conocimiento)

# Consulta al agente lógico
consulta = "lluvia"
resultado = agente.realizar_inferencia(consulta)

# Imprimir el resultado de la consulta
if resultado:
    print(f"El agente lógico ha inferido que '{consulta}' es cierto.")
else:
    print(f"El agente lógico ha inferido que '{consulta}' es falso.")
