class Board:
    def __init__(self):
        # Initializes a list of 9 empty spaces
        self.state = [' ' for _ in range(9)]

    def print_board(self):
        print("\n")
        print(f" {self.state[0]} | {self.state[1]} | {self.state[2]} ")
        print("---+---+---")
        print(f" {self.state[3]} | {self.state[4]} | {self.state[5]} ")
        print("---+---+---")
        print(f" {self.state[6]} | {self.state[7]} | {self.state[8]} ")
        print("\n")

    def is_space_free(self, position):
        return self.state[position] == ' '

    def insert_letter(self, position, letter):
        if self.is_space_free(position):
            self.state[position] = letter
            return True
        return False

    def is_board_full(self):
        return ' ' not in self.state

    def check_win(self, letter):
        s = self.state
        # All possible winning combinations
        win_conditions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8), # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8), # Columns
            (0, 4, 8), (2, 4, 6)             # Diagonals
        ]
        for condition in win_conditions:
            if s[condition[0]] == s[condition[1]] == s[condition[2]] == letter:
                return True
        return False
