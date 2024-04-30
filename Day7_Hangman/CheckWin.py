import random
word_list = ["ardvark", "baboon", "camel"]

word = random.choice(word_list)
#Testing code
print(f'Pssst, the solution is {word}.')
display = []
for i in range(0,len(word)):
    display.append("_")

#TODO-1: - Use a while loop to let the user guess again.
#The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
end = False
while not end:
    letter = input("Guess a letter: ").lower()
    for j in range(0,len(word)):
        if letter == word[j]:
            display[j] = letter
    print(display)
    if "_" not in display:
        end = True
        print("You've won")
