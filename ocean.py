
height=float(input("Enter your height:"))
price=0
if height>=4:
    print("You are eligible for water games")
    age=int(input("Please enter age"))
    if age>=10 and age<=15:
        price+=20
        # print(price)
        gender=input("Please enter gender").upper()
        if gender=="M":
            price+=3
            print(price)
        if gender=="F":
            price+=5    
            print(price)
        combo=(input("You want combo Y,N")).upper()
        if combo=="Y":
            price+=10
            print(f"Your final price is{price}")
        if  combo=="N":
            print(price)  
    elif age>=16 and age<=25:
        price+=30
        print(price)    
    elif age>=25 and age<=60:
        print(f"you have a free ride with {price}")    
else:
    print("Not eligible")    