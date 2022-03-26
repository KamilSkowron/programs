import random
def guess_player(x):
    number = random.randint(1,x)
    counter = 0
    guess = None
    while guess != number:
        guess = int(input("Guess the number: "))
        counter += 1
        if guess > number:
            print("Lower!")
        elif guess < number:
            print("Higher!")
    print("{} is the number! You guess after a {} time!".format(guess,counter))

def guess_computer_smart(x, y):
    low = 1
    high = x
    mid = None
    counter = 0
    while mid != y:
        counter += 1
        mid = (high+low)//2
        if mid > y:
            high = mid
        if mid < y:
            low = mid
    print("I guessed your number ({}) after {} time".format(y,counter))
    
guess_computer_smart(1000,392)

def guess_computer_random(x,y):
    low = 1
    high = x
    guess = None
    counter = 0
    while guess != y:
        guess = random.randint(low, high)
        counter += 1
        if guess > y:
            high = guess
        elif guess < y:
            low = guess
    print("I guessed your number ({}) after {} time".format(y,counter))

guess_computer_random(1000,392)
