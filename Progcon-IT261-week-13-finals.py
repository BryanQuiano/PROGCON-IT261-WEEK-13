
def display_board(board):
  print(f"{board[1]} | {board[2]} | {board[3]}")
  print("-+-+-")
  print(f"{board[4]} | {board[5]} | {board[6]}")
  print("-+-+-")
  print(f"{board[7]} | {board[8]} | {board[9]}")


def check_winner(board):
  result = "None"
  filled_count = 0

  if board[1] != " " and board[1] == board[2] and board[2] == board[3]:
    result = board[1]
  elif board[4] != " " and board[4] == board[5] and board[5] == board[6]:
    result = board[4]
  elif board[7] != " " and board[7] == board[8] and board[8] == board[9]:
    result = board[7]
  elif board[1] != " " and board[1] == board[4] and board[4] == board[7]:
    result = board[1]
  elif board[2] != " " and board[2] == board[5] and board[5] == board[8]:
    result = board[2]
  elif board[3] != " " and board[3] == board[6] and board[6] == board[9]:
    result = board[3]
  elif board[1] != " " and board[1] == board[5] and board[5] == board[9]:
    result = board[1]
  elif board[3] != " " and board[3] == board[5] and board[5] == board[7]:
    result = board[3]

  for k in range(1, 10):
    if board[k] != " ":
      filled_count += 1

  if result == "None" and filled_count == 9:
    result = "Draw"

  return result


def get_computer_move(board):
  valid = False
  while not valid:
    comp_move = random.randint(1, 9)
    if board[comp_move] == " ":
      valid = True
  return comp_move


def main():
  board = [""] * 10
  for i in range(1, 10):
    board[i] = " "

  game_over = False
  winner = "None"
  r = random.randint(0, 1)

  current_player = "O" if r == 0 else "X"

  while not game_over:
    display_board(board)

    if current_player == "O":
      valid_move = False
      while not valid_move:
        try:
          human_move = int(input("Enter your move (1-9): "))
          if 1 <= human_move <= 9:
            if board[human_move] == " ":
              valid_move = True
            else:
              print("Space occupied! Try again.")
          else:
            print("Invalid choice! Enter 1-9.")
        except ValueError:
          print("Invalid input! Please enter a number between 1 and 9.")
      board[human_move] = "O"
    else:
      print("Computer's turn...")
      comp_choice = get_computer_move(board)
      board[comp_choice] = "X"

    winner = check_winner(board)

    if winner != "None":
      game_over = True
    else:
      current_player = "X" if current_player == "O" else "O"

  display_board(board)

  if winner == "O":
    print("You win!")
  elif winner == "X":
    print("Computer wins!")
  else:
    print("It's a draw!")


if __name__ == "__main__":
  main()
