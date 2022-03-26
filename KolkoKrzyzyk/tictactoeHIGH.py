import random
from abc import ABC, abstractclassmethod

class Game:

    board = [" " for i in range(9)]

    def show(self):
        print(f"{self.board[0]} | {self.board[1]} | {self.board[2]}\n----------\n{self.board[3]} | {self.board[4]} | {self.board[5]}\n----------\n{self.board[6]} | {self.board[7]} | {self.board[8]}")
        print("")
    
    def available(self):
        taken = {(i+1) for i in range(9) if ('O' == self.board[i] or 'X' == self.board[i])}
        avaible = {(i+1) for i in range(9)} - taken
        return avaible
    
    def check_win(self):
        board_2d = [[self.board[i] for i in range(3)],[self.board[i+3] for i in range(3)],[self.board[i+6] for i in range(3)]]
        
        counter_X = 0
        counter_O = 0
    
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
                print("Player O won!")
                exit()
            if counter_X == 3:
                print("Player X won!")
                exit()

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
                print("Player O won!")
                exit()
            if counter_X == 3:
                print("Player X won!")
                exit()

        #diagonal check
        counter_O = 0
        counter_X = 0
        for i in range(3):
            if board_2d[i][i] == 'X':
                counter_X += 1
            if board_2d[i][i] == 'O':
                counter_O += 1
        if counter_O == 3:
            print("Player O won!")
            exit()
        if counter_X == 3:
            print("Player X won!")
            exit()
  
        #antydiagonal check
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
                print("Player O won!")
                exit()
            if counter_X == 3:
                print("Player X won!")
                exit()

    def mark_X(self,player):
        self.board[player-1] = 'X'
        self.show()
        self.check_win()

    def mark_O(self,player):
        self.board[player-1] = 'O'
        self.show()
        self.check_win()

    def play(self,p1,p2):
        self.show()
        self.mark_X(p1.choose())
        while len(self.available()) > 0:
            self.mark_O(p2.choose())
            self.mark_X(p1.choose())
        print("It's a tie!")

game = Game()

class Player:
    @abstractclassmethod
    def choose(self):
        pass

class Human(Player):
    def choose(self):
        p_c = None
        while p_c not in Game().available():
           
            try:
                p_c = int(input("Your move, choose spot(1-9): "))
                if p_c in Game().available():
                    return p_c
                else:
                    print("Wrong input, choose one of: {}".format(Game().available()))
                
            except Exception as e:
                print("Error message: "+str(e))
                print("Wrong input, choose one of: {}".format(Game().available()))
        
class Computer(Player):
    def choose(self):
        p_c = random.choice(list(Game().available()))
        return p_c

human = Human()
computer = Computer()

game.play(human,computer)