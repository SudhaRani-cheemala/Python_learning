# # # def rec_count(number):
# # #     print(number)
# # #     if number==0:
# # #         return 0
# # #     rec_count(number-1)
# # #     print(number)
# # # rec_count(5)    
# # # -----------------------------Recursive----------------------
# # def factorial(x):
# #     if x==1:
# #         return 1
# #     else:
# #         return(x*factorial(x-1))
# # num=3
# # print(factorial(3))   


# def rec_count(number):
#     print(number)
#     # Base case
#     if number == 0:
#         return 0
#     rec_count(number - 1)  # A recursive call with a different argument
#     print(number)


# rec_count(5)

# # ----------------
dir_var={" ":"sudha"}
print(dir_var.keys())
print(type(dir_var))