
board = ['-','-','-',
         '-','-','-',
         '-','-','-']
#game
current_player = "X"
game_is_still_going = True
winner = None
def display_board():
  print()
  print(board[0]+" | "+board[1]+" | "+board[2])
  print(board[3]+" | "+board[4]+" | "+board[5])
  print(board[6]+" | "+board[7]+" | "+board[8])
  print("\n")

#flip_player()
def play_game():
  display_board()

  while game_is_still_going:
    handle_turn(current_player)
    check_if_the_game_is_over()
    flip_player()
  if winner =='X' or winner =="O":
    print(winner+"'s won")
  else:
    print("Tie")

def check_if_the_game_is_over():
  check_for_the_winner()
  check_for_tie()


def handle_turn(current_player):
  print(current_player+"'s turn")
  
  position = input("Choose a position of 1-9 : " )
  
  vaild = False
  while not vaild:
    
    while position not in ["0","1","2","3","4","5","6","7","8"]:
      position = input("Choose a position of 1-9 : " )
    position = int(position) - 1
    if board[position] =="-":
      vaild= True
    else:
      print("you can't go there.")

  board[position] = current_player
  display_board()
  

def check_for_the_winner():
  global winner
  row_winner = check_row_winner()
  colum_winner = check_colum_winner()
  diagonal_winner = check_diagonal_winner()
  if row_winner:
    winner = row_winner
  elif colum_winner:
    winner = colum_winner
  else:
    winner = diagonal_winner


def check_row_winner():
  global game_is_still_going
  row_1 = board[0]==board[1]==board[2] != "-"
  row_2 = board[3]==board[4]==board[5] != "-"
  row_3 = board[6]==board[7]==board[8] != "-"
  if row_1 or row_2 or row_3:
    game_is_still_going = False
  if row_1:
    return board[0]
  elif row_2:
    return board[3]
  elif row_3:
    return board[6]
  else:
    return None
def check_colum_winner():
  global game_is_still_going
  colum_1 = board[0]==board[3]==board[6] != "-"
  colum_2 = board[2]==board[4]==board[7] != "-"
  colum_3 = board[3]==board[5]==board[8] != "-"
  if colum_1 or colum_2 or colum_3:
    game_is_still_going = False
  if colum_1:
    return board[0]
  elif colum_2:
    return board[2]
  elif colum_3:
    return board[3]
  else:
    return None
def check_diagonal_winner():
  global game_is_still_going
  diagonal_1 = board[0]==board[4]==board[8] != "-"
  diagonal_2 = board[2]==board[4]==board[6] != "-"
  if diagonal_1 or diagonal_2:
    game_is_still_going = False
  if diagonal_1:
    return board[0]
  elif diagonal_2:
    return board[2]
  else:
    return None



def check_for_tie():
  global game_is_still_going
  if "-" not in board:
    game_is_still_going  = False
    return True
  else:
    return 
def flip_player():
  global current_player
  if current_player=="X":
    current_player="O"
  elif current_player=="O":
    current_player="X"


play_game()
        
