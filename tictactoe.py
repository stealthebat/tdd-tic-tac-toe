class TicTacToe:

    def __init__(self):
        self.board = [' '] * 9
        self.current_player = 'X'
        self.winner = None

    def is_game_over(self):
        return self.winner is not None or ' ' not in self.board

    def get_winner(self):
        return self.winner

    def get_current_player(self):
        return self.current_player

    def get_board(self):
        return self.board

    def make_move(self, position):
        self.board[position-1] = self.current_player
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def print_board(self):
        for i in range(3):
            print(*self.board[i*3:3*i+3])


def main():
    game = TicTacToe()


if __name__ == '__main__':
    main()
