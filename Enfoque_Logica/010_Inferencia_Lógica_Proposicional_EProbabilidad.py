class InferenciaLogicaProposicional:
    def __init__(self, base_conocimiento):
        self.base_conocimiento = base_conocimiento

    def inferir(self, objetivo):
        for regla in self.base_conocimiento.reglas:
            antecedente_verificado = True
            for hecho in regla.antecedente:
                if hecho not in self.base_conocimiento.hechos:
                    antecedente_verificado = False
                    break
            if antecedente_verificado:
                if objetivo in regla.consecuente:
                    return True
        return False

# Ejemplo de uso
from collections import namedtuple

# Definimos la base de conocimiento
Hecho = namedtuple("Hecho", ["nombre"])
Regla = namedtuple("Regla", ["antecedente", "consecuente"])

base_conocimiento = {
    "hechos": {Hecho("p"), Hecho("q")},
    "reglas": {
        Regla({Hecho("p")}, {Hecho("r")}),
        Regla({Hecho("q")}, {Hecho("r")})
    }
}

# Creamos el motor de inferencia lógica
motor_inferencia = InferenciaLogicaProposicional(base_conocimiento)

# Realizamos inferencias
print("¿Se puede inferir r?")
print(motor_inferencia.inferir(Hecho("r")))  # True
print("¿Se puede inferir s?")
print(motor_inferencia.inferir(Hecho("s")))  # False
