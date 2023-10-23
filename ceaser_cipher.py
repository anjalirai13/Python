alphabet = list(set({"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
          "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"}))

import pdb

direction = raw_input("Type decode for decyrption or encode fro encryption to perform operation\n").lower()
print("direction is ",direction)
message = raw_input("Enter the message\n").lower()
print("text is ",message)


shift = int(input("Enter the number you want to shift\n"))

def encryp(plain_text,shift_amount):
  cipher_text=""
  for letter in plain_text :
    position= alphabet.index(letter)
    new_position= position+shift_amount
    new_letter=alphabet[new_position]
    cipher_text += new_letter
    print(cipher_text)
  print("{cipher_text} is encoded")


encryp(message, shift)