import random
import os

path = "score.txt"

choices = ["rock"
, "paper", "scissors"]

player_score = 0
computer_score = 0

while True:
    again = None
    player = None
    while player not in choices:
        player = input("paper/rock/scissors? ")
    computer = random.choice(choices)

    print("Player: \t",player)
    print("Computer: \t",computer)
    
    if player == computer:
        print("It's a tie!")

    elif player == "rock":
        if computer == "paper":
            print("You lose!")
            computer_score += 1
        else: 
            print("You won!")
            player_score += 1

    elif player == "paper":
        if computer == "scissors":
            print("You lose!")
            computer_score += 1
        else: 
            print("You won!")
            player_score += 1

    else:
        player == "scissors"
        if computer == "rock":
            print("You lose!")
            computer_score += 1
        else: 
            print("You won!")
            player_score += 1
    
    again = input("Do you wanna play again?(yes/no): ")
    if again.lower() != "yes" and again.lower() != "y":
        break

if os.path.exists(path):
    with open(path,'r') as file:
        z = file.read()
        x, y = z.split('|')
        w1 = int(x) + player_score
        w2 = int(y) + computer_score
        print("Player: " +str(w1)+ " | Computer: "+str(w2))

    with open(path,'w') as file:
        text =  str(w1)+ "|" +str(w2)
        file.write(str(text))

else:
    with open(path,'w') as file:
        w1 = player_score
        w2 = computer_score
        text =  str(w1)+ "|" +str(w2)
        file.write(str(text))
        

input()