# if the bill was $150,split b/w 5 people with 12% tip
# 
print("Welcome to the Tip calculator")
bill=float(input("Wht aws the total bill?"))
tip=int(input("How much tip would you like to give"))
people=int(input("How many people are their to share"))
tip_as_percentage=tip/100
total_tip_amount=bill*tip_as_percentage
total_bill=bill+total_tip_amount
bill_per_person=total_bill/people
final_amount=round(bill_per_person,2)
print(final_amount)

