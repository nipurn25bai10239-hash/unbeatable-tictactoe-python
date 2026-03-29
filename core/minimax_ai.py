import math

def minimax(board, depth, is_maximizing):
    # Base cases: Check if the game is over and return a score
    if board.check_win('O'): return 10 - depth
    if board.check_win('X'): return depth - 10
    if board.is_board_full(): return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board.is_space_free(i):
                board.state[i] = 'O'
                score = minimax(board, depth + 1, False)
                board.state[i] = ' ' # Undo the move
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board.is_space_free(i):
                board.state[i] = 'X'
                score = minimax(board, depth + 1, True)
                board.state[i] = ' ' # Undo the move
                best_score = min(score, best_score)
        return best_score

def get_best_move(board):
    best_score = -math.inf
    best_move = -1
    for i in range(9):
        if board.is_space_free(i):
            board.state[i] = 'O'
            score = minimax(board, 0, False)
            board.state[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
    return best_move
