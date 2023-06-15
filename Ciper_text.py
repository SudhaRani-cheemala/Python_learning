normal_text=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
direction=input("type encode to encrypt ,type decode to decrypt")
text=input("Enter text")
ln=print(len(normal_text))
shift=int(input("Type the shift number :"))
def encrypt(plaintext,shift_amount):
    ciper_text=""
    if shift_amount<=len(normal_text):
        for letter in plaintext:
         position=normal_text.index(letter)
         new_position=position+shift_amount
         new_letter=normal_text[new_position]
         ciper_text+=new_letter
        print(ciper_text)  
    else:
      print("Index is out of range")  
encrypt(plaintext=text,shift_amount=shift)    