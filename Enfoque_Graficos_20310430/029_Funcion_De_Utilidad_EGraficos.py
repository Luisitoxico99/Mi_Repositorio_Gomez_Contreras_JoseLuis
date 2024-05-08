# Definición de la clase para representar un juego de lotería
class LotteryGame:
    def __init__(self, prize, probability):
        self.prize = prize  # Premio de la lotería
        self.probability = probability  # Probabilidad de ganar el premio

# Función de utilidad esperada para evaluar una lotería
def expected_utility(lottery):
    return lottery.prize * lottery.probability

# Ejemplo de juego de lotería
lottery_A = LotteryGame(prize=1000, probability=0.5)  # Una lotería con premio de $1000 y probabilidad de ganar del 50%
lottery_B = LotteryGame(prize=2000, probability=0.3)  # Otra lotería con premio de $2000 y probabilidad de ganar del 30%

# Calcular la utilidad esperada de cada lotería
utility_A = expected_utility(lottery_A)
utility_B = expected_utility(lottery_B)

# Imprimir los resultados
print("Utilidad esperada de la lotería A:", utility_A)
print("Utilidad esperada de la lotería B:", utility_B)

# Tomar la decisión basada en la utilidad esperada
if utility_A > utility_B:
    print("Se recomienda elegir la lotería A.")
elif utility_A < utility_B:
    print("Se recomienda elegir la lotería B.")
else:
    print("Ambas loterías tienen la misma utilidad esperada. La elección depende de otras consideraciones.")
