import numpy as np

def init_board():
  board = np.empty(shape=(3,3), dtype='object')
  for r in range(3):
    for c in range(3):
      board[r][c] = " "
  return board

def draw_board():
 print(board[0][0] + '|' + board[0][1] + '|' + board[0][2])
 print("-----")
 print(board[1][0] + '|' + board[1][1] + '|' + board[1][2])
 print("-----")
 print(board[2][0] + '|' + board[2][1] + '|' + board[2][2])

def update_board(row, col, piece):
  board[row][col] = piece

def is_empty(row, col):
  return board[row][col] == " "

def check_win(piece):
  #check horizontal
  for r in range(3):
    if (board[r][0] == piece and board[r][1] == piece and board[r][2] == piece):
      return True
  #check vertical
  for c in range(3):
    if (board[0][c] == piece and board[1][c] == piece and board[2][c] == piece):
      return True
  #main diagonal
  if (board[0][0] == piece and board[1][1] == piece and board[2][2] == piece):
    return True
  
  #other diagonal
  if (board[0][2] == piece and board[1][1] == piece and board[2][0] == piece):
    return True

def check_tie():
  for row in range(3):
    for col in range(3):
      if is_empty(row, col):
        return False
  return True
    
  

board = init_board()

turn = 0
piece = 'X'
gameover = False

#GAME LOOP
while not gameover:
  if turn == 0:
    row = int(input("P1 enter a row (1-3): ")) - 1
    col = int(input("P1 enter a column (1-3): ")) - 1
  if turn == 1:
    row = int(input("P2 enter a row (1-3): ")) - 1
    col = int(input("P2 enter a column (1-3): ")) - 1

  

  while not is_empty(row, col):
    print("Not a valid move. Try again.")
    if turn == 0:
      row = int(input("P1 enter a row (1-3): ")) - 1
      col = int(input("P1 enter a column (1-3): ")) - 1
    if turn == 1:
      row = int(input("P2 enter a row (1-3): ")) - 1
      col = int(input("P2 enter a column (1-3): ")) - 1
  
  update_board(row, col, piece)
  draw_board()

  #check win
  if (check_win(piece)):
    gameover = True
    print("P{} WINS!!".format(turn + 1))
  
  #check tie
  if (check_tie()):
    gameover = True
    print("There is a tie.")


  turn += 1
  turn = turn % 2

  if piece == 'X':
    piece = 'O'
  else:
    piece = 'X'



  















