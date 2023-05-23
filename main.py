def print_board(board):
  print("   |   |   ")
  print(" " + board[0] + " | " + board[1] + " | " + board[2] + " ")
  print("___|___|___")
  print("   |   |   ")
  print(" " + board[3] + " | " + board[4] + " | " + board[5] + " ")
  print("___|___|___")
  print("   |   |   ")
  print(" " + board[6] + " | " + board[7] + " | " + board[8] + " ")
  print("   |   |   ")


def get_move(player):
  valid_move = False
  while not valid_move:
    move = input(player + ", enter a number between 1 and 9: ")
    if move.isdigit() and int(move) >= 1 and int(move) <= 9:
      valid_move = True
    else:
      print("Invalid input. Please enter a number between 1 and 9.")
  return int(move) - 1


def check_win(board):
  win_combos = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7],
                [2, 5, 8], [0, 4, 8], [2, 4, 6]]
  for combo in win_combos:
    if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ':
      return board[combo[0]]
  if ' ' not in board:
    return 'tie'
  return None


def play_game():
  board = [' '] * 9
  current_player = 'X'
  winner = None

  while not winner:
    print_board(board)
    move = get_move(current_player)
    if board[move] == ' ':
      board[move] = current_player
      if current_player == 'X':
        current_player = 'O'
      else:
        current_player = 'X'
    else:
      print("That space is already taken.")
    winner = check_win(board)

  print_board(board)
  if winner == 'tie':
    print("It's a tie!")
  else:
    print("Congratulations, " + winner + "! You win.")


play_game()
