import random
from words import word, words_animal_pl, words_animal, HANGMANPICS
# from words import word_animal

def valid_word():
    #choose_word = random.choice(word)
    #choose_word = random.choice(words_animal)
    choose_word = random.choice(words_animal_pl)

    while '-' in choose_word or ' ' in choose_word:
        choose_word = random.choice(word)
    return choose_word

def hangman():
    lives = 7
    word = valid_word().upper()
    list_used = {""}
    list_word = list(word)

    list_guess = []
    for index in range(len(list_word)):
        list_guess.append("_")
    while (list_guess != list_word):
        good = False
        print("Used letters: ",end="")
        print(*list_used)
        print("\nYou have {} lifes".format(lives))
        print(HANGMANPICS[-lives])
        print(*list_guess)

        guess = input("Guess a letter: ").upper()

        for i in range(len(list_word)):
            if guess == list_word[i]:
                list_guess[i] = guess
                good = True  
        if (good == False) or (guess in list_used):
            lives -= 1
            if lives == 0:
                print("You lose!")
                quit()

        list_used.add(guess)
          
    print("")
    print(*list_guess,end=" was the word.\n")
    print("Congratulations, you won!")

hangman()


