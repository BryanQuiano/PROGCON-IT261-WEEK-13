def __init__(self):
    self.board = [" "] * 10
    self.current_player = random.choice(["O", "X"])

  def display_board(self):
    print()
    print(f" {self.board[1]} | {self.board[2]} | {self.board[3]} ")
    print("---+---+---")
    print(f" {self.board[4]} | {self.board[5]} | {self.board[6]} ")
    print("---+---+---")
    print(f" {self.board[7]} | {self.board[8]} | {self.board[9]} ")
    print()

  def check_winner(self):
    winning_combinations = [
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),  # Rows
        (1, 4, 7),
        (2, 5, 8),
        (3, 6, 9),  # Columns
        (1, 5, 9),
        (3, 5, 7),  # Diagonals
    ]

    for a, b, c in winning_combinations:
      if (
          self.board[a] == self.board[b] == self.board[c]
          and self.board[a] != " "
      ):
        return self.board[a]

    if " " not in self.board[1:]:
      return "Draw"

    return None

  def get_computer_move(self):
    available_spots = [i for i, spot in enumerate(self.board[1:], 1) if spot == " "]
    return random.choice(available_spots)

  def play(self):
    print("--- Welcome to Tic-Tac-Toe! ---")
    print("You are 'O' and the Computer is 'X'.")
    print(f"Random draw: '{self.current_player}' goes first!\n")

    while True:
      self.display_board()
      winner = self.check_winner()

      if winner:
        if winner == "Draw":
          print("It's a draw!")
        elif winner == "O":
          print("You win!")
        else:
          print("Computer wins!")
        break

      if self.current_player == "O":
        try:
          move = int(input("Enter your move (1-9): "))
          if 1 <= move <= 9:
            if self.board[move] == " ":
              self.board[move] = "O"
              self.current_player = "X"
            else:
              print("Space occupied! Try again.")
          else:
            print("Invalid choice! Enter a number between 1 and 9.")
        except ValueError:
          print("Invalid input! Please enter a number.")
      else:
        print("Computer's turn...")
        move = self.get_computer_move()
        self.board[move] = "X"
        self.current_player = "O"


if __name__ == "__main__":
  game = TicTacToe()
  game.play()
