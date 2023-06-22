import random
def deal_cards():
    """" returns a random card from the deck"""
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card
def calculate_score(cards):
    print(f"my cards are {cards}")
    """ Take a list of cards and return the score calculated from the cards"""
    # sum is a in built function for summation
    print(len(cards))
    print(sum(cards))
    if sum(cards)==21 or len(cards)==2:
      return 0
    # if the card sum reaches the count of 21 then the ace card should take the value as 1 not the high value as 11 so 
    # have to remove 11 and append 1 
    if 11 in cards and sum(cards)>21:
       cards.remove(11)
       cards.append(1)
       return sum(cards)
user_cards=[]
computer_cards=[]   
is_game_over=False 
for _ in range(2):
    new_card=deal_cards()
    user_cards.append(new_card)
    print(f"my user cards are {user_cards}")
    computer_cards.append(deal_cards())
    # inside calculate score check for blackjack(a hand with only 2 cards:ace+10 and retirn 0 here 0 will represent the 
    #  jack in our game)   
while not is_game_over:   
    user_score=calculate_score(user_cards)
    print(f"my user score is{user_score}")
    computer_score=calculate_score(computer_cards)  
    print(f"your cards are {user_cards},current score:{user_score}")
    print(f"Computers first card:{computer_score}")
    if user_score==0 or computer_score==0 or user_score >21 :
        is_game_over=True  
    else:
        user_should_deal=input("Type 'y' to get another card,type 'n' to pass:")
    if user_should_deal=="y":
        print(user_cards)
        user_cards.append(deal_cards())
    else:
        is_game_over=True   
        