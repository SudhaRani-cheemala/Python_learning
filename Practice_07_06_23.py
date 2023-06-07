welcome=input("Welcome to the rollercoastr!!!")
print(welcome)
user_height=int(input("Please enter height"))
bill=0
if user_height>=120:
    print("You are eligible to ride rollercosater")
    user_age=int(input("Please enter age of the participants:"))
    if user_age<=12:
        print("Your entry fee is $5")
        bill+=5
    elif user_age<=18:
        print("Your entry fee is $7")
        bill+=7
    elif user_age>=45 and user_age<=55:
        bill+=0
        print("Your enty fee is free")      
    else:
        print("you are not eliguble for free ride")  
    photo = input("Do you want photo Y or N")
    if photo == "Y":
        bill+=3
        print(f"your final bill {bill}")          
else:
    print("You are not eligible")    