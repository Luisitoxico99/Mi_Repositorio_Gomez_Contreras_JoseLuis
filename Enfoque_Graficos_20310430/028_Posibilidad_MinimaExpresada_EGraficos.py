import random

# Definición de la clase para el juego de azar
class Game:
    def __init__(self):
        self.current_state = 0  # Estado inicial del juego

    def get_possible_moves(self):
        # Retorna una lista de movimientos posibles (números aleatorios entre 1 y 6 para un dado)
        return [random.randint(1, 6) for _ in range(3)]  # Simplemente como ejemplo, el jugador puede lanzar el dado tres veces

    def get_next_state(self, move):
        # Retorna el siguiente estado del juego basado en el movimiento realizado (en este caso, la suma de los lanzamientos de dados)
        return self.current_state + move

    def is_game_over(self):
        # Retorna True si el juego ha terminado (por ejemplo, si se alcanza una cierta puntuación)
        return self.current_state >= 15  # Ejemplo de condición de finalización del juego

# Función de evaluación para el juego de azar
def evaluate(game, depth):
    if game.is_game_over() or depth == 0:
        return game.current_state  # Valor del estado actual del juego como evaluación
    else:
        possible_moves = game.get_possible_moves()
        # Calcular el valor esperado para cada movimiento basado en las probabilidades de los posibles resultados
        expected_values = []
        for move in possible_moves:
            next_state = game.get_next_state(move)
            expected_value = evaluate(Game(next_state), depth - 1)
            expected_values.append(expected_value)
        return sum(expected_values) / len(expected_values)  # Valor esperado como evaluación

# Función para seleccionar el mejor movimiento utilizando Minimax Esperado
def get_best_move(game, depth):
    possible_moves = game.get_possible_moves()
    best_move = None
    best_value = float('-inf')
    for move in possible_moves:
        next_state = game.get_next_state(move)
        value = evaluate(Game(next_state), depth - 1)
        if value > best_value:
            best_value = value
            best_move = move
    return best_move

# Ejemplo de juego utilizando Minimax Esperado
def play_game():
    game = Game()
    while not game.is_game_over():
        print("Estado actual del juego:", game.current_state)
        move = get_best_move(game, depth=2)  # Profundidad de búsqueda para Minimax Esperado
        print("Se realiza el movimiento:",
