import tkinter as tk

class TicTacToe:
    def __init__(self):  # ✅ Fixed constructor
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_widgets()

    def create_widgets(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col] = tk.Button(
                    self.root,
                    text="",
                    font=("Arial", 20),
                    width=5,
                    height=2,
                    command=lambda r=row, c=col: self.on_click(r, c)
                )
                self.buttons[row][col].grid(row=row, column=col)

        self.score_label = tk.Label(
            self.root,
            text="Player X's Turn",
            font=("Arial", 14)
        )
        self.score_label.grid(row=3, column=0, columnspan=3, pady=5)

        self.restart_button = tk.Button(
            self.root,
            text="Restart Game",
            font=("Arial", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            padx=10,
            pady=5,
            command=self.reset_board
        )
        self.restart_button.grid(row=4, column=0, columnspan=3, pady=10)

    def on_click(self, row, col):
        if self.buttons[row][col]["text"] == "":
            self.buttons[row][col]["text"] = self.current_player
            self.buttons[row][col]["fg"] = "#1976D2" if self.current_player == "X" else "#E91E63"

            if self.check_winner():
                self.score_label.config(text=f"Game Over - Player {self.current_player} wins!")
                self.disable_buttons()
            elif self.check_draw():
                self.score_label.config(text="Game Over - It's a draw!")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.score_label.config(text=f"Player {self.current_player}'s Turn")

    def check_winner(self):
        for i in range(3):
            if self.buttons[i][0]["text"] == self.buttons[i][1]["text"] == self.buttons[i][2]["text"] != "":
                return True
            if self.buttons[0][i]["text"] == self.buttons[1][i]["text"] == self.buttons[2][i]["text"] != "":
                return True
        if self.buttons[0][0]["text"] == self.buttons[1][1]["text"] == self.buttons[2][2]["text"] != "":
            return True
        if self.buttons[0][2]["text"] == self.buttons[1][1]["text"] == self.buttons[2][0]["text"] != "":
            return True
        return False

    def check_draw(self):
        for row in self.buttons:
            for button in row:
                if button["text"] == "":
                    return False
        return True

    def reset_board(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col]["text"] = ""
                self.buttons[row][col]["fg"] = "black"
                self.buttons[row][col].config(state=tk.NORMAL)
        self.current_player = "X"
        self.score_label.config(text="Player X's Turn")

    def disable_buttons(self):
        for row in self.buttons:
            for button in row:
                button.config(state=tk.DISABLED)

    def run(self):
        self.root.mainloop()

# ✅ Start the game
game = TicTacToe()
game.run()