class EncadenamientoHaciaAtras:
    def __init__(self, base_conocimiento, meta):
        self.base_conocimiento = base_conocimiento
        self.meta = meta

    def inferir(self, meta):
        if meta in self.base_conocimiento.hechos:
            return True
        for regla in self.base_conocimiento.reglas:
            if meta in regla.consecuente:
                if all(self.inferir(antecedente) for antecedente in regla.antecedente):
                    return True
        return False

# Creamos el motor de encadenamiento hacia atrás
motor_encadenamiento_atras = EncadenamientoHaciaAtras(base_conocimiento, Hecho("r"))

# Realizamos inferencias
resultado = motor_encadenamiento_atras.inferir(Hecho("r"))
print("¿Se puede inferir 'r'?", resultado)
