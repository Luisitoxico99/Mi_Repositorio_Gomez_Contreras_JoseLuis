import numpy as np

class Game:
    def __init__(self, payoff_matrix):
        self.payoff_matrix = payoff_matrix

    def find_nash_equilibrium(self):
        # Encontrar las estrategias mixtas que maximizan el pago esperado para cada jugador
        player1_payoffs = np.max(self.payoff_matrix, axis=1)
        player2_payoffs = np.max(self.payoff_matrix, axis=0)

        # Encontrar los índices de las estrategias mixtas que maximizan el pago esperado para cada jugador
        player1_strategies = np.where(self.payoff_matrix == np.max(self.payoff_matrix, axis=1)[:, None])[1]
        player2_strategies = np.where(self.payoff_matrix == np.max(self.payoff_matrix, axis=0))[0]

        # Encontrar los equilibrios de Nash como las estrategias mixtas que maximizan el pago esperado para ambos jugadores
        nash_equilibria = set(zip(player1_strategies, player2_strategies))

        return nash_equilibria

class Mechanism:
    def __init__(self, nash_equilibrium):
        self.nash_equilibrium = nash_equilibrium

    def induce_cooperation(self):
        # Si el equilibrio de Nash incluye la cooperación mutua, mantener esa estrategia
        if (0, 0) in self.nash_equilibrium:
            return "Ambos jugadores cooperan."
        # Si no, ofrecer un incentivo para la cooperación mutua
        else:
            return "Ofrecer un beneficio adicional para la cooperación mutua."

# Matriz de pagos del juego
payoff_matrix = np.array([[3, 1],
                           [4, 2]])

# Crear el juego
game = Game(payoff_matrix)

# Encontrar el equilibrio de Nash
nash_equilibrium = game.find_nash_equilibrium()

# Crear el mecanismo
mechanism = Mechanism(nash_equilibrium)

# Inducir el comportamiento deseado
behavior = mechanism.induce_cooperation()

# Imprimir el resultado
print("Equilibrio de Nash:", nash_equilibrium)
print("Mecanismo para inducir cooperación:", behavior)
