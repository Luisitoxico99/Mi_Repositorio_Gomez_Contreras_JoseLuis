def evaluate(board):
    # Verificar si el jugador X gana
    if board.is_winner('X'):
        return 1
    # Verificar si el jugador O gana
    elif board.is_winner('O'):
        return -1
    # Si no hay ganador pero el tablero está lleno, es un empate
    elif board.is_full():
        return 0
    else:
        # Calcular la puntuación basada en la cantidad de fichas en línea para cada jugador
        score = 0
        # Considerar las filas y columnas
        for i in range(3):
            row_count_X = board.board[i].count('X')
            row_count_O = board.board[i].count('O')
            col_count_X = sum(1 for j in range(3) if board.board[j][i] == 'X')
            col_count_O = sum(1 for j in range(3) if board.board[j][i] == 'O')
            score += (row_count_X - row_count_O) + (col_count_X - col_count_O)
        # Considerar las diagonales
        diag1_count_X = sum(1 for i in range(3) if board.board[i][i] == 'X')
        diag1_count_O = sum(1 for i in range(3) if board.board[i][i] == 'O')
        diag2_count_X = sum(1 for i in range(3) if board.board[i][2 - i] == 'X')
        diag2_count_O = sum(1 for i in range(3) if board.board[i][2 - i] == 'O')
        score += (diag1_count_X - diag1_count_O) + (diag2_count_X - diag2_count_O)
        return score
