
normal_text = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
text=input("Type your message:")
shift=int(input("Enter shift number:\n"))
def Decrypt(ciper_text,shift_amount):
    plain_text=""
    for letter in ciper_text:
        position=normal_text.index(letter)
        new_position=position-shift_amount
        plain_text+=normal_text[new_position]
    print(f"The decoded text is {plain_text}")    
Decrypt(ciper_text=text,shift_amount=shift)    