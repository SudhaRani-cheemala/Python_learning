# Rock Paper Scissors ASCII Art

# Rock
import random
Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
images = [Rock , Paper, Scissors]
user_choice=int(input("What do you choose?Type 0 for Rock,1 for Paper,2 for Scissors \n"))
print(images[user_choice])
computer_choice=random.randint(0,2)
print("Computer choice:")
print(images[computer_choice])
# print(f"Computer choice {computer_choice}")
if user_choice==0 and computer_choice==2:
    print("User wins!")
elif computer_choice==0 and user_choice==2:
    print("You lose!")    
elif computer_choice>user_choice:
    print("Computer wins!")
elif computer_choice==user_choice:
    print("its a draw")    
elif computer_choice<=2:
    print(images[2])    
else:
    print("you typed an invalid number,you lose?")
