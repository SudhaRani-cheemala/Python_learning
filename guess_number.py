# choosing a random number
from random import randint
from art1 import logo
EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5
turns=0
# function to check user's guess against actual answer

def check_answer(guess,answer,turns):
    """ Checks answer against guess.Returns the number of turns remaining."""
    if guess>answer:
        print("Too High")
        return turns -1
    elif guess<answer:
        print("Too low")
        return turns -1
    else:
        print(f"You got it your answer was {answer}")        
#   make a function to set difficulty
def set_difficulty():
    level=input("Choose a difficulty. Type 'easy' or 'hard':")
    if level=='easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS    
def game():     
    print(logo)
    print("Welcome to the guessing game!!!")
    print("Iam thinking of a number between 1 to 100")
    answer=randint(1,100)

    print(f"the correct answer is {answer}")    

    # let the user guess a number
    guess=int(input("Make a guess:"))
    turn=set_difficulty()
    print(f"You have {turn} attempts remaining to guess the number")   
    guess=0
    while guess!=answer:
        guess=int(input("guess the number:")) 
        # updates local variable turns every turn
        turn=check_answer(guess,answer,turn)
        if turn==0:
            print("Reached maximum atempts")
            return
        elif guess!=answer:
            print("Start guess again")   

game()      
# track the number of turnsand reduce by 1 if they get it wrong
# repeat the guessing functionality if they get it wron
