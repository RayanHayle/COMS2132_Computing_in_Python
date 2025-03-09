# STEPS: 
#1. randomly pick a word from the file ✅
#2. let user enter 5-letter word  ✅
#3. if word not in file --> quit ✅
#4. if char correct and correct space --> green ✅
#5. if char correct not in correct space --> yellow✅
#6. if char wrong --> gray✅
#7. keep track of guesses - 6 attempts✅

import random
from colorama import Fore, Back, Style, init  # pip install colorama
init(autoreset=True)  # initialize the coloring

########## Step 1: Read, Pick Word ###########
def SelectWord():
    with open("wordle.txt", 'r') as file:
        Reading_Text = file.read()
        the_word = Reading_Text.split()
        position_word = random.randint(0, len(the_word)-1)
        TheWordGuess = the_word[position_word]
    return TheWordGuess.strip().lower()

######### Step 2: Guess user input, exist on control c ############
def UserGuess():
    TheWordToGuess = SelectWord()
    try:
        user_guess = input("Please type a 5-letter word(letters only): ")
        return user_guess.lower()
    except KeyboardInterrupt:
        print("\nCtrl+C pressed, exiting...")
        print(f"The word was: {TheWordToGuess}")
        exit(0)

######### Step 3: Compare both words using colorama ############

def ColorCompare():
    TheWordToGuess = SelectWord()
    attempts = 0
    #print(f"the guess word hint: {TheWordToGuess}")

    while attempts <6:
    
        TheUserGuess = UserGuess()
        result = [None] * 5  # Result = [None, None, None, None, None], change it to color index by index
        
        # 1. guess only from valid words in file
        with open("wordle.txt", 'r') as file:
            valid_words = file.read().split()

        # 2. make sure length is 5 and word is valid: does not reset guess count
        if len(TheUserGuess) != 5 or TheUserGuess not in valid_words:
            print("Please enter a valid 5-letter word.")
            continue
        
        # 3. guessed correct word = all green char
        if TheUserGuess == TheWordToGuess:
            #print(Fore.GREEN + Style.RESET_ALL)
            print("".join([Back.GREEN + char + Style.RESET_ALL for char in TheUserGuess]))
            print("Congratulations")
            break

        # 4. correct char, correct position = green
        for i in range(5):
            if TheUserGuess[i] == TheWordToGuess[i]: 
                result[i] = Back.GREEN + TheUserGuess[i] + Style.RESET_ALL
                        
        # 5. correct char, wrong position = yellow
        for i in range(5):
            if result[i] is None:  # an index value is None meaning yellow or gray
                if TheUserGuess[i] in TheWordToGuess:
                    result[i] = Back.YELLOW + TheUserGuess[i] + Style.RESET_ALL

                # 6. wrong char, wrong position = gray (using ANSI escape code beacuse Back.Gray does not work)
                else:
                    result[i] = '\033[48;5;235m' + TheUserGuess[i] + Style.RESET_ALL  

        print(" ".join(result))
        
        # Decrease attempts
        attempts += 1
        print(f"Guesses: {attempts} /6")

    # If out of attempts
    if attempts == 6:
        print(f"Game over! The word was: {Fore.GREEN}{TheWordToGuess}{Style.RESET_ALL}")

if __name__="__main__":
    ColorCompare()
