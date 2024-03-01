import random
import time

def computer_turn(board):
    while True:
        row = random.randint(0, 7)
        column = random.randint(0, 7)
        position = f"{chr(65 + column)}{row + 1}"  # Convert row and column to position format
        if board[row][column] not in ['|S', '|G', '*']:
            return position
def print_board(board):
    a=' ABCDEFGH'
    for i in list(a):
        print(i,end='|')
    print()
    for i in range(0, 8):
        print(i+1,end='|')
        for j in range(0, 8):
            print(board[i][j],end='|')
        print() 
def update_board(board, position, value):
    column_mapping = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}
    row = int(position[1]) - 1
    column = column_mapping[position[0].upper()] - 1
    if board[row][column] != '-':
        return False
    if row in range(8) and column in range(8):
        board[row][column] = value
    else:
        print("Invalid position. Please enter a position within the board range.")
def check_hit(turn,board5,board6):
    column_mapping = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}
    row = int(turn[1]) - 1
    column = column_mapping[turn[0].upper()] - 1
    if  board5[row][column] == 'S':
        print('You HIT The Ship')
        board6[row][column] = '|S'
    elif board5[row][column] == 'G' :
        print('You Hit the gernade')
        board6[row][column] = '|G'
        return False
    else:
        print('You missed it')
        board6[row][column] = '*'
def check_winner(board1):
    f=0
    for i in range(8):
        for j in range(8):
            if board1[i][j] == '|S':
                f += 1
    if f == 6:
        return True
    else:
        return False
board = [['-' for _ in range(8)] for _ in range(8)] # player will work in it
board1 = [['-' for _ in range(8)] for _ in range(8)] #it will be showed to oppsite player
board3 = [['-' for _ in range(8)] for _ in range(8)] # player will work in it
board4 = [['-' for _ in range(8)] for _ in range(8)] #it will be showed to oppsite player
i=0
print_board(board)
while i<6:
    print('Where you want to place your SHIP')
    position = input("Enter position (e.g., A1, B2): ")
    if update_board(board, position, 'S') == False:
        print('position already occupied')
        time.sleep(2)
    else:
        update_board(board, position, 'S')
        i+=1
    print_board(board) 
i=0 
print_board(board)
while i<4:
    print('Where you want to place your Greanade')
    position = input("Enter position (e.g., A1, B2): ")
    if update_board(board, position, 'G') == False:
        print('position already occupied')
        time.sleep(2)
    else:
        update_board(board, position, 'G')
        i+=1
    print_board(board) 
print('PLAYER 2')
time.sleep(2)
i=0
print_board(board3)
while i<6:
    print('Where you want to place your SHIP')
    position = input("Enter position (e.g., A1, B2): ")
    if update_board(board3, position, 'S') == False:
        print('position already occupied')
        time.sleep(2)
    else:
        update_board(board3, position, 'S')
        i+=1
    print_board(board3) 
i=0 
print_board(board3)
while i<4:
    print('Where you want to place your Greanade')
    position = input("Enter position (e.g., A1, B2): ")
    if update_board(board3, position, 'G') == False:
        print('position already occupied')
        time.sleep(2)
        
    else:
        update_board(board3, position, 'G')
        i+=1
    print_board(board3)
G= True
F= True 
while True:
    if G==False:
        print('you missed this turn')
        G=True
    else:
        print('player 1 turn')
        print('player 2 board looks like')
        print_board(board4)
        turn = input('enter position where you want to target')
        G=check_hit(turn,board3,board4)
        if check_winner(board3) == True:
            print('Player 1 won')
            break
    if F==False:
        print('you missed this turn')
        F=True
    else:
        print('player 2 turn')
        print('player 1 board looks like')
        print_board(board1)
        turn = input('enter position where you want to target')
        F=check_hit(turn,board,board1)
        if check_winner(board1) == True:
            print('Player 2 won')
            break




