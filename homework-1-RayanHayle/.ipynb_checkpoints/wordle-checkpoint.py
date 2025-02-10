import random
def SelectWord():
 print('opening file')
    with open ("wordle.txt", 'r') as file:
        Reading_Text = file.read()
	print('read file')
        the_word = Reading_Text.split()
	print('split at white space')
        position_word = random.randint(0, len(the_word)-1)
        print(f' The word is: {the_word[position_word]}')    
