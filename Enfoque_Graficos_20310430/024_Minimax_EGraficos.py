# Definición del juego de tic-tac-toe
class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]  # Tablero vacío de 3x3
        self.current_player = 'X'  # Jugador actual (X comienza)

    def print_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-----')

    def is_winner(self, player):
        # Revisa filas y columnas
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)) or \
               all(self.board[j][i] == player for j in range(3)):
                return True
        # Revisa diagonales
        if all(self.board[i][i] == player for i in range(3)) or \
           all(self.board[i][2 - i] == player for i in range(3)):
            return True
        return False

    def is_full(self):
        return all(self.board[i][j] != ' ' for i in range(3) for j in range(3))

    def is_game_over(self):
        return self.is_winner('X') or self.is_winner('O') or self.is_full()

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        return False

# Función Minimax
def minimax(board, depth, is_maximizing):
    if board.is_winner('X'):  # Si X gana, devuelve un puntaje positivo
        return 1
    elif board.is_winner('O'):  # Si O gana, devuelve un puntaje negativo
        return -1
    elif board.is_full() or depth == 0:  # Si es un empate o se alcanza la profundidad máxima
        return 0

    if is_maximizing:
        max_eval = float('-inf')  # Inicializar el valor máximo como infinito negativo
        for i in range(3):
            for j in range(3):
                if board.board[i][j] == ' ':
                    board.board[i][j] = 'X'  # Prueba una jugada para X
                    eval = minimax(board, depth - 1, False)
                    board.board[i][j] = ' '  # Deshacer la jugada
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')  # Inicializar el valor mínimo como infinito positivo
        for i in range(3):
            for j in range(3):
                if board.board[i][j] == ' ':
                    board.board[i][j] = 'O'  # Prueba una jugada para O
                    eval = minimax(board, depth - 1, True)
                    board.board[i][j] = ' '  # Deshacer la jugada
                    min_eval = min(min_eval, eval)
        return min_eval

# Función para tomar la mejor jugada para el jugador X
def get_best_move(board):
    best_eval = float('-inf')
    best_move = None
    for i in range(3):
        for j in range(3):
            if board.board[i][j] == ' ':
                board.board[i][j] = 'X'  # Prueba una jugada para X
                eval = minimax(board, 5, False)  # Profundidad máxima de búsqueda
                board.board[i][j] = ' '  # Deshacer la jugada
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)
    return best_move

# Función principal para jugar al tic-tac-toe
def play_game():
    game = TicTacToe()
   
