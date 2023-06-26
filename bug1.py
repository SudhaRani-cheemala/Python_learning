# age=int(input("How old are you??"))
# if we dont give age as int it will show error
# if age>18:
#     print(f"Yoiu are eligible for driving {age}")
# pages=0
# w_p_p=0
# pages=int(input("number of pages"))
# # if we put == instead of = it will throw an error
# w_p_p=int(input("Number of words"))
# total_words=pages*w_p_p
# print(pages,w_p_p)
# print(total_words)
# ---------------------------------------------------------------------
# def mutate(a_list):
#     b_list=[]
#     for item in a_list:
#         new_item=item*2
#         b_list.append(new_item)
#         print(b_list)
# mutate([1,2,3,5,8,13])        
#------------------------------------------------------------------
# num=int(input("Enter a number:"))
# if num%2==0:
#   print("Number is even")
# else:
#   print("Odd number")  
# --------------------------------------------------------------------
# year=int(input("Enter a year"))
# if year%4==0:
#     if year%100==0:
#         if year%400==0:
#             print("Leap year")
#         else:
#             print("Not a leap year")
#     else:
#         print("Leap year")
# else:
#     print("Not a leap year")   
#----------------------------------------------------------------------
for number in range(1,101):
    if number %3==0 or number%5==0:
        print("FizzBuzz")
    if number%3==0:
        print("Fizz") 
    if number%5==0:
        print("Buzz")
    else:
        print(number)                    