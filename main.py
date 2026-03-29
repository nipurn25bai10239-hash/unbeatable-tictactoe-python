from core.board import Board
from core.minimax_ai import get_best_move

def play_game():
    board = Board()
    print("Welcome to Minimalist Tic-Tac-Toe AI!")
    print("Positions are mapped 1-9 (Top-Left is 1, Bottom-Right is 9).")
    board.print_board()

    while not board.is_board_full():
        # Human Player's Turn
        valid_move = False
        while not valid_move:
            try:
                move = int(input("Enter your move (1-9): ")) - 1
                if 0 <= move <= 8 and board.is_space_free(move):
                    board.insert_letter(move, 'X')
                    valid_move = True
                else:
                    print("Invalid move. Space is taken or out of range.")
            except ValueError:
                print("Please enter a valid number.")

        board.print_board()
        
        if board.check_win('X'):
            print("You win! (Wait, this is mathematically impossible...)")
            break
        if board.is_board_full():
            print("It's a tie!")
            break

        # AI's Turn
        print("AI is calculating its optimal move...")
        ai_move = get_best_move(board)
        board.insert_letter(ai_move, 'O')
        board.print_board()

        if board.check_win('O'):
            print("AI wins! Mathematical perfection achieved.")
            break
        if board.is_board_full():
            print("It's a tie!")
            break

if __name__ == "__main__":
    play_game()
