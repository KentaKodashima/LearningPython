import random

def clear_output():
  print('\n'*100)


def display_board(board):
  clear_output()
  print(board[0] + '|' + board[1] + '|' + board[2])
  print(board[3] + '|' + board[4] + '|' + board[5])
  print(board[6] + '|' + board[7] + '|' + board[8])


def player_input():
  marker = ''

  while (marker != 'X' and marker != 'O'):
    marker = input('Player 1: Choose X or O: ').upper()
  
  player1 = marker
  player2 = ''

  if player1 == 'X':
    player2 = 'O'
  else:
    player2 = 'X'

  return (player1, player2)


def place_marker(board, marker, position):
  board[position-1] = marker


def win_check(board, mark):
  if (board[0] == mark and board[1] == mark and board[2] == mark or
      board[3] == mark and board[4] == mark and board[5] == mark or
      board[6] == mark and board[7] == mark and board[8] == mark or
      board[0] == mark and board[3] == mark and board[6] == mark or 
      board[1] == mark and board[4] == mark and board[7] == mark or 
      board[2] == mark and board[5] == mark and board[8] == mark or
      board[0] == mark and board[4] == mark and board[8] == mark or
      board[2] == mark and board[4] == mark and board[6] == mark):
    return True
  else:
    return False


def choose_first():
  coin = random.randint(0,1)
  if (coin == 0):
    return 'Player 1'
  else:
    return 'Player 2'


def space_check(board, position):
  return board[position-1] == ' '


def full_board_check(board):
  for i in range(1,10):
    if (space_check(board,i)):
      return False
  return True


def player_choice(board):
  choice = -1

  while (choice not in range(0,10)):
    choice = int(input('Please enter a number to mark (1-9): '))

  while (not space_check(board, choice)):
    input('The position is already marked. Please enter another number: ') 

  return choice
  

def replay():
  answer = ''

  while (answer.lower() not in ['yes', 'no']):
    answer = input('Do you want to keep playing? (Yes or Nn): ')
    if (answer not in ['yes', 'no']):
      print('I could not understand the option. Please choose from Yes ot No.')

  return answer.lower() == 'yes'



# ==========
# Game logic
# ==========
print('Welcome to Tic Tac Toe!')

while (True):
  game_board = [' ']*10
  player1, player2 = player_input()
  turn = choose_first()
  print(turn + ' goes first.')

  play_game = input('Ready to play? y or n: ')
  game_on = play_game == 'y'

  while (game_on):
    if (turn == 'Player 1'):
      display_board(game_board)
      choice = player_choice(game_board)
      game_board[choice-1] = player1
      if win_check(game_board, player1):
        print('Player 1 won the game!')
        game_on = False
      turn = 'Player 2'
    else:
      display_board(game_board)
      choice = player_choice(game_board)
      game_board[choice-1] = player2
      win_check(game_board, player2)
      if win_check(game_board, player2):
        print('Player 2 won the game!')
        game_on = False
      turn = 'Player 1'

    if (full_board_check(game_board)):
      print('Drawn game.')
      game_on = False

  if (not replay()):
    print('The end of the game.')
    break