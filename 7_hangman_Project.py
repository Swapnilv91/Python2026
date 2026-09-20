#HangMan Project Stepwise

import random

#Step 1 chose the word from the list 
word_list = ["sharvil","rajdhani","camel"]
chosen_word = random.choice(word_list)
print(chosen_word)

guess = input("Guess the alphabet: ").lower()

for i in chosen_word:
    if i == guess :
        print("Match")
    else:
        print("No match")