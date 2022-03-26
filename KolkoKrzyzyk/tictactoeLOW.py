import random
import time

board = [i+1 for i in range(9)]
print(f"{board[0]} | {board[1]} | {board[2]}\n----------\n{board[3]} | {board[4]} | {board[5]}\n----------\n{board[6]} | {board[7]} | {board[8]}")

board = [" " for i in range(9)]

def mark_X(w):
    board[w-1] = "X"
    z = print(f"{board[0]} | {board[1]} | {board[2]}\n----------\n{board[3]} | {board[4]} | {board[5]}\n----------\n{board[6]} | {board[7]} | {board[8]}")
    return z

def mark_O(w):
    board[w-1] = "O"
    z = print(f"{board[0]} | {board[1]} | {board[2]}\n----------\n{board[3]} | {board[4]} | {board[5]}\n----------\n{board[6]} | {board[7]} | {board[8]}")
    return z

def free():
    taken = {""}
    for i in range(9):
        if ('O' == board[i] or 'X' == board[i]):
            taken.add(i+1)
    return taken

def player_choose():
    p_c = int(input("Your move, choose spot(1-9): "))
    
    while (p_c in free() or p_c> 9 or p_c < 1):
        print("You can't pick there, try somewhere else:\n")
        p_c = int(input("Your move, choose spot(1-9): ")) 
    return p_c

def computer_choose():
    p_c = random.randrange(1,9)
    
    while (p_c in free()):
        p_c = random.randrange(1,9)
    return p_c

def win_check():
    counter_X = 0
    counter_O = 0
    board_2d = [[board[i] for i in range(3)],[board[i+3] for i in range(3)],[board[i+6] for i in range(3)]]
    
    #horizontal check
    for i in range(3):
        counter_O = 0
        counter_X = 0
        for j in range(3):
            if board_2d[i][j] == 'X':
                counter_X += 1
            if board_2d[i][j] == 'O':
                counter_O += 1
        if counter_O == 3:
            print("Computer won!")
            return 0
        if counter_X == 3:
            print("Player won!")
            return 1

    #vertical check
    for j in range(3):
        counter_O = 0
        counter_X = 0
        for i in range(3):
            if board_2d[i][j] == 'X':
                counter_X += 1
            if board_2d[i][j] == 'O':
                counter_O += 1
        if counter_O == 3:
            print("Computer won!")
            return 0
        if counter_X == 3:
            print("Player won!")
            return 1

    #diagonal check
    counter_O = 0
    counter_X = 0
    for i in range(3):
        if board_2d[i][i] == 'X':
            counter_X += 1
        if board_2d[i][i] == 'O':
            counter_O += 1
    if counter_O == 3:
        print("Computer won!")
        return 0
    if counter_X == 3:
        print("Player won!")
        return 1
  
    # #antydiagonal check
    counter_O = 0
    counter_X = 0
    for i in range(3):
        for j in range(3):
            if i+j == 2:
                if board_2d[i][j] == 'X':
                    counter_X += 1
                if board_2d[i][j] == 'O':
                    counter_O += 1
        if counter_O == 3:
            print("Computer won!")
            return 0
        if counter_X == 3:
            print("Player won!")
            return 1

def game():
    
    
    while {'',1,2,3,4,5,6,7,8,9} != free():
        

        mark_X(player_choose())
        if win_check() == 1 or win_check() == 0:
            break
        
        if {'',1,2,3,4,5,6,7,8,9} == free():
            print("It's a tie!")
            break

        print("\n#########\n")
        
        time.sleep(0.5)
        mark_O(computer_choose())
        if win_check() == 1 or win_check() == 0:
            break

game()