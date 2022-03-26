questions ={"How many days do we have in a week?":"A",
            "How many days are there in a normal year?":"B",
            "Which animal is called King of Jungle?":"C",
            "What is the top color in a rainbow?":"D",
            "What type of bird lays the largest eggs?":"A"}

answers = [["A. Seven","B. Six","C. Five","D. Eight"],
           ["A. 356","B. 365","C. 366","D. 367"],
           ["A. Octopus","B. Kangaroo","C. Lion","D. Tiger"],
           ["A. Yellow","B. Green","C. Blue","D. Red"],
           ["A. Ostrich","B. Snake","C. Chicken","D. Dog"]]

dict_items = list(questions.items())

def new_game():

    score = 0
    print("")
    for index in range(len(questions)):
        print(str(index+1)+". "+dict_items[index][0])
        
        for row in range(len(questions)-1):
            print(answers[index][row])
        guess = input("Answer: ")

        if guess.upper() == dict_items[index][1]:
            print("CORRECT!\n")
            score += 1
        else:
            print("WRONG!\n")
    print("You knew {} of {} questions!".format(score,len(questions)))

def again():
    
    while True:
        d = input("Do you wanna play again?(yes/no): ")
        if d.lower() == "yes" or d.lower() == "y":
            new_game()
        else:
            break

new_game()
again()
