import random
word_list=["aravar","ball","cat"]
choose_word=random.choice(word_list)
print(f"choosen word is: {choose_word}")
display=[]
word_length=len(choose_word)
for _ in range(word_length):
    display+="-"  
    end_of_game=False    
while not end_of_game:    
    guess=input("Guess a letter:").lower()
    for position in range(word_length):
        letter=choose_word[position]
        if letter==guess:
            display[position]=letter
print(display)    
if "-" not in display:
    end_of_game=True
    print("You win")
    
