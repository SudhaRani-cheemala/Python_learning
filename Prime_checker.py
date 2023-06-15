# num=int(input("Enter a number"))
def prime_checker(num):
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                print("Number is not a  prime")
                break
        else:
            print("Number is a prime")
prime_checker(73)