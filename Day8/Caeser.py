alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift, direction):
    end_text = ""
    if direction == "decode":
        shift *= -1
    for letter in start_text:
        position = alphabet.index(letter)
        new_position = position + shift
        end_text += alphabet[new_position]
    print(f"Here's the {direction}d result: {end_text}")

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
if direction == "encode" or direction == "decode":
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text,shift,direction)
else:
    
    print(f"Thats not a direction to do. Try again. Encode or Decode") 