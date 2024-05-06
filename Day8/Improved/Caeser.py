from art import logo


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)
def caesar(start_text, shift, direction):
    if shift > 25:
        shift += -26 
    end_text = ""
    if direction == "decode":
        shift *= -1
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift
            end_text += alphabet[new_position]
        else:
            end_text += letter
    print(f"Here's the {direction}d result: {end_text}")
end = False
while end == False: 
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction == "encode" or direction == "decode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(text,shift,direction)
    else:
        print(f"Thats not a direction to do. Try again. Encode or Decode") 
    tryagain = input("Continue? [Y/N] ").lower()
    if tryagain == "n":
        end = True
