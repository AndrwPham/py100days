import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["ardvark", "baboon", "camel"]

word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {word}.')

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
#TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."
#TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
lives = 6
display = []
for i in range(0,len(word)):
    display.append("_")

end = False
while not end:
    duplicate = False
    check_char = False
    print(stages[lives])
    letter = input("Guess a letter: ").lower()
    for char in display:
        if letter == char:
            duplicate = True     #Check if you retype the same letter
    for j in range(0,len(word)):
        if letter == word[j]:
            display[j] = letter
            check_char = True
    if not check_char or duplicate:
        lives -= 1 
    print(f"{' '.join(display)}") #Join the list into a string
    if lives <= 0:
        end= True
        print("You've lost")
    elif "_" not in display:
        end = True
        print("You've won")
