# STEPS: 
#1. randomly pick a word form the file ✅

#2. let user enter 5 letter word  
#    - if word not in file --> quit 

#3. if letter correct and correct space--> green
#4. if letter correct not in correct space --> yellow
#5. keep track of guesses 

import random

def SelectWord():
    with open ("wordle.txt", 'r') as file:
        Reading_Text = file.read() .file(new_file, delimiter = ';') 
        the_word = Reading_Text.split()
        position_word = random.randint(0, len(the_word)-1)
        #print(f' The word is: {the_word[position_word]}')  
    return position_word



def UserGuess():
    TheWord = SelectWord()
    print(TheWord)
    user_guess = input('Please type a 5-letter word(letters only): ')

    if user_guess == TheWord:
        print("Congratulations")

    while user_guess != TheWord:
        pass
        
    
