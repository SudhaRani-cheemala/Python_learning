normal_text = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
text = input("Enter text: ")
shift = int(input("Type the shift number: "))

def encrypt(plaintext, shift_amount):
 cipher_text = ""
 for letter in plaintext:
  position = normal_text.index(letter) if letter in normal_text else -1
  if position != -1:
   new_position = (position + shift_amount) % len(normal_text)
   new_letter = normal_text[new_position]
   cipher_text += new_letter
 else:
  cipher_text += str(position)
  print(cipher_text)

encrypt(plaintext=text, shift_amount=shift)


