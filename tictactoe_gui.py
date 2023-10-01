import tkinter as tk
from tkinter import messagebox
from tictactoe import TicTacToe


class TicTacToeGUI:

    def __init__(self):
        self.game = TicTacToe()
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.create_board()
        self.input_frame = tk.Frame(self.root)
        self.cur_player = tk.Label(self.input_frame, width=10, text="Turn: " + self.game.current_player)
        self.cur_player.pack(side=tk.TOP)
        self.entry = tk.Entry(self.input_frame, width=10)
        self.entry.pack(side=tk.TOP)
        self.button = tk.Button(self.input_frame, text="Make Move", command=self.make_move)
        self.button.pack(side=tk.TOP)
        self.input_frame.grid(row=3, column=0, columnspan=3, pady=(5, 0))

    def create_board(self):
        for i in range(3):
            for j in range(3):
                entry = tk.Label(self.root, width=10, text="_")
                entry.grid(row=i, column=j)

    def update_board(self):
        self.cur_player["text"] = "Turn: " + self.game.current_player
        board = self.game.get_board()
        for i in range(3):
            for j in range(3):
                self.root.grid_slaves(row=i, column=j)[0]["text"] = board[i*3+j]

    def make_move(self):
        position = self.entry.get()
        self.entry.delete(0, tk.END)
        try:
            self.game.make_move(position)
            self.update_board()
            if self.game.is_game_over():
                winner = self.game.get_winner()
                if winner:
                    messagebox.showinfo("Game Over", f"Player {winner} wins!")
                else:
                    messagebox.showinfo("Game Over", "It's a draw!")
                self.root.destroy()
        except (IndexError, ValueError) as e:
            messagebox.showerror("Invalid Move", str(e))

    def start(self):
        self.root.mainloop()


def main():
    gui = TicTacToeGUI()
    gui.start()


if __name__ == "__main__":
    main()
