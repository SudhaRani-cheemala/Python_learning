from art import logo
from game_data import data
import random
# from replit import clear

# display the art
print(logo)
"""format the account data into printable format"""
def format_data(account):
    account_name=account["name"]
    account_des=account["description"]
    account_country=account["country"]
    return f"{account_name},{account_des},{account_country}"
"""Take the user guess and followers counts and returns if they gotit right."""
def check_answer(guess,a_folloers,b_followers):
    if a_folloers>b_followers:
        return guess=="a"
    else:
        return guess=="b"

score=0
game_should_contiue=True
account_b=random.choice(data)
# make the game repeatable
while game_should_contiue:
    # clear()
    # generate random account from game data
    account_a=account_b
    account_b=random.choice(data)
    if account_a==account_b:
        account_b=random.choice(data)
    print(f"Compare A:{format_data(account_a)}.")
    print(f"Compare B:{format_data(account_b)}.")    

    # ask user for a guess
    guess=input("Who has more followers A or B:").lower()
    # check if user is correct
    # get followers count of each account
    a_follower_count=account_a["follow_count"]
    b_follower_count=account_b["follow_count"]
    is_correct=check_answer(guess,a_follower_count,b_follower_count)
    # score keeping
    if is_correct:
        score+=1
        print(f"You are right!!! Current score : {score}.")
    else:
        game_should_contiue=False
        print(f"Sorry, that's wrong.Final score:{score}.")    

# use if statement to check if user is correct
# give user feedback on their guess


# Making account at position B become the next accout at position B
# Clear the screen between rounds