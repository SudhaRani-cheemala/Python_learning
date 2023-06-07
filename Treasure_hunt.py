print("welcome to the treasure isaland")
print("your mission isnto find treasure")
# to ignore case sensitivity giving upper case
choice=input("Choose left or right L,R \n").upper()
if choice=="L":
    print("Game is started")
    ch=input("swim or wait S W").upper()
    if ch=="S":
        print("Game over")
    if ch=="W":
        color=input("Which door? R B Y").upper()
        if color=="R" or "B":
            print("GAME OVER")
        if color=="Y":
            print("YOU WIN")
else:
    print("Game is not possible")    