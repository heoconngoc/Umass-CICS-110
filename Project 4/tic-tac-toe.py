# Author   : Quoc Dat Pham
# Email    : quocdatpham@umass.edu
# Spire ID : 34740949

def print_board(n, board):
  # premake +---+ style boundary using string mutiplication and concatination
  boundary_line = ("+---" * n) + "+"
  # range over every row in board (an n by n board)
  for i in range(n):
    # print a leading boundary line
    print(boundary_line)
    # start string for row i with leading bar
    row_i = "|"
    # range over every column in board (an n by n board)
    for j in range(n):
      # update row_i string with space, characher from board, space, and trailing bar
      # this completes "cell j" for row i
      row_i += " " + board[i][j] + " " + "|"
    # print the completed row i
    print(row_i)
  # print final boundary line
  print(boundary_line)

def make_empty_board(n):
    board = []  
    for i in range(n):
        row = [] 
        for j in range(n):
            row.append(' ')  
        board.append(row)  
    return board 

def get_location(n,game_board):
  while True:
    r = input(f'Please enter a row index between 0 and {n-1}: ')
    c = input(f'Please enter a column index between 0 and {n-1}: ')
    if not r.isdigit() or not c.isdigit():
      print(f'({r}, {c}) is not a legal input!')
      continue
    r= int(r)
    c= int(c)
    if r < 0 or r >= n or c < 0 or c >= n:
      print(f'({r}, {c}) is not a legal space!')
      continue
    if game_board[r][c] != ' ':
      print(f'({r}, {c}) is not an available space!')
      continue
    break
  return r,c

def row_win(n, game_board, player):
  row_result = [player] * n
  for row in game_board:
    if row == row_result:
      return True
  return False    

def col_win(n, game_board, player):
    for i in range(n):
        result = True
        for row in game_board:
            if row[i] != player:
                result = False
                break
        if result:
            return True
    return False
    

def diag_win(n, game_board, player):
  for i in range(n):
    if game_board[i][i] != player:
      return False
  return True

def anti_diag_win(n, game_board, player):
  for i in range(n):
    if game_board[i][n-1-i] != player:
      return False
  return True

def has_won(n, game_board, player):
  if row_win(n, game_board, player) or col_win(n, game_board, player) or diag_win(n, game_board, player) or anti_diag_win(n, game_board, player): 
    return True 
  return False

# print(has_won(3, make_empty_board(3), 'X'))
# # >>> False
# print(has_won(3, [['O', 'O', 'O'], [' ', 'X', 'X'], [' ', ' ', 'X']], 'O')) #row
# # >>> True
# print(has_won(3, [['O', ' ', ' '], ['O', 'X', ' '], ['O', 'X', 'X']], 'O')) #col
# # >>> True
# print(has_won(3, [['X', 'O', 'O'], [' ', 'X', ' '], [' ', ' ', 'X']], 'X')) #diag
# # >>> True
# print(has_won(3, [['O', 'O', 'X'], [' ', 'X', ' '], ['X', ' ', ' ']], 'X')) #anti_diag
# # >>> True

def isFull(n, board):
  for row in range(n):
    for col in range(n):
      if board[row][col] == ' ':
        return False
  return True
      

def play_game(n):
  print(f'*** Welcome to {n} by {n} Tic-Tac-Toe ***')
  board = make_empty_board(n)
  print_board(n,board)
  current = 'X'

  while True:
    print(f"* {current}'s turn *")
    
    r, c = get_location(n,board)
    board[r][c] = current
    print_board(n,board)

    if has_won(n, board, current):
      print(f'{current} wins!')
      break
    if isFull(n, board):
      print('Tie!')
      break

    if current == "X":
        current = "O"
    else:
        current = "X"

play_game(2)