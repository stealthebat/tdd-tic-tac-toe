import unittest
from tictactoe import TicTacToe


class TicTacToeTest(unittest.TestCase):

    def test_initial_state(self):
        game = TicTacToe()
        self.assertIsNotNone(game.get_board())
        self.assertEqual(game.get_board(), [' '] * 9)
        self.assertEqual(game.get_current_player(), 'X')
        self.assertIsNone(game.get_winner())

    def test_make_move(self):
        game = TicTacToe()
        game.make_move(1)
        self.assertEqual(game.get_current_player(), 'O')
        self.assertEqual(game.get_board()[0], 'X')


if __name__ == '__main__':
    unittest.main()