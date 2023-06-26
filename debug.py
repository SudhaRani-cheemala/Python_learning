# def my_fun():
#   for i in range(1,20):
#     # bug bcz it will not take 20 as index till 19 only it will take
#     if i==20:
#       print("You got it")
# my_fun()      
# ---------------------------------------------------------------
# from random import randint
# dice_images=["1","2","3","4","5","6"]
# # here error came bcz of index issue and list always takes index from 0 only 
# # right one is (0,5)
# dice_num=randint(1,6)
# print(dice_images[dice_num])
# -------------------------------------------------------------------------

year=int(input("What is your year of birth"))
year=1994
if year>1980 and year <1994:
    print("You are a millenial")
elif year >=1994:
    print("You are a Gen Z.")
