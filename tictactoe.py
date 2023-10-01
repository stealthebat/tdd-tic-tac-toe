class TicTacToe:

    def __init__(self):
        self.board = ['_'] * 9
        self.current_player = 'X'
        self.winner = None

    def is_game_over(self):
        return self.winner is not None or '_' not in self.board

    def get_winner(self):
        return self.winner

    def get_current_player(self):
        return self.current_player

    def get_board(self):
        return self.board

    def print_board(self):
        for i in range(3):
            print(*self.board[i*3:3*i+3])

    def make_move(self, position):
        try:
            position = int(position)
        except ValueError as e:
            raise ValueError("Enter a number!") from e
        if not 1 <= position <= 9:
            raise IndexError("Enter a number in range [1, 9]!")
        if self.board[position - 1] != '_':
            raise ValueError("Invalid move!")

        self.board[position-1] = self.current_player
        self.check_winner()
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]

        for combination in winning_combinations:
            a, b, c = combination
            if self.board[a] == self.board[b] == self.board[c] != '_':
                self.winner = self.current_player
                break


def main():
    game = TicTacToe()
    while not game.is_game_over():
        print("Turn:", game.get_current_player())
        try:
            move = input("Input a cell number in range [1; 9]: ")
            game.make_move(move)
        except (IndexError, ValueError) as e:
            print(str(e))
        print("Board:")
        game.print_board()
        print()

    if game.get_winner():
        print("Winner:", game.get_winner() + "!")
    else:
        print("Draw!")
    input()


if __name__ == '__main__':
    main()
