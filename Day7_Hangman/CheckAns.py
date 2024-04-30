#Checking if the input letter is match or not
import random
#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
word_list = ["ardvark", "baboon", "camel"]

word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {word}.')

letter = input("Guess a letter: ").lower()

for char in word:
    if letter == char:
        print("Right")
    else:
        print("Wrong")