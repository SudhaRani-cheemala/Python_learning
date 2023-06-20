from art import logo
print(logo)
bids={}
bidding_finished=False
def find_hight_bidder(bidder_record):
 highest_bid=0
 for bidder in bidder_record:
  bid_amout=bidder_record[bidder]
  if bid_amout >highest_bid:
   highest_bid=bid_amout
   winner=bidder 
   print(f"the winner is {winner} with a bid of {highest_bid}") 
 
while not bidding_finished:
 name=input("What is your name???")
 price=int(input("What is the bidding price"))
 bids[name]=price
 should_continue=input("Are there any other bidders? type 'yes' or 'no'")
 if should_continue=="no":
  bidding_finished=True
  find_hight_bidder(bids)
 elif should_continue=="yes":
  print("hghhh")
#   clear()  
  