import random
from hangman_wordlist import word_list
from hangman_art import logo
from hangman_art import stages
#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py

#TODO-2: - Import the stages from hangman_art.py and make this error go away.

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.


word = random.choice(word_list)
print(logo)
#Testing code
print(f'Pssst, the solution is {word}.')

lives = 6
display = []
for i in range(0,len(word)):
    display.append("_")

end = False
while not end:
    duplicate = False
    check_char = False
    
    letter = input("Guess a letter: ").lower()
    for char in display:
        if letter == char:
            duplicate = True     #Check if you retype the same letter
    for j in range(0,len(word)):
        if letter == word[j]:
            display[j] = letter
            check_char = True
    if not check_char: 
        print(f"You guessed {letter}, thats not in the word.")
        lives -= 1 
    if duplicate:
        print(f"You have guessed letter {letter} before.")
        lives -= 1
    print(f"{' '.join(display)}") #Join the list into a string
    print(stages[lives])
    if lives <= 0:
        end= True
        print("You've lost")
    elif "_" not in display:
        end = True
        print("You've won")
