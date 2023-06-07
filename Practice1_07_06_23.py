print("Welcome to python deliveries!")
size=input("Enter size of the pizza? S,M,L  ")
price=0
if size=="S":
    price+=15
    add_pepporoni=input("Do you want pepporoni? Y or N")
    if add_pepporoni=="Y":
        price+=2
        print(price)
    extra_cheese=input("Do you want extra cheese? Y or N")
    if extra_cheese=="Y":
        price+=3   
        print(price)
        print(f"Your final bill is {price}")
elif size=="M":
    price+=20
    add_pepporoni=input("Do you want pepporoni? Y or N")
    if add_pepporoni=="Y":
        price+=2
        print(price)
    extra_cheese=input("Do you want extra cheese? Y or N")
    if extra_cheese=="Y":
        price+=3   
        print(price)
        print(f"Your final bill is {price}")
elif size=="L":
    price+=25
    add_pepporoni=input("Do you want pepporoni? Y or N")
    if add_pepporoni=="Y":
        price+=2
        print(price)
    extra_cheese=input("Do you want extra cheese? Y or N")
    if extra_cheese=="Y":
        price+=3   
        print(price)   
        print(f"Your final bill is {price}")
else:
    print("Entered size of pizza is not avalable")
