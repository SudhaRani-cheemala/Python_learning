import random
letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q']
numbers=['1','2','3','4','5','6','7','8','9','10','11']
symbols=['@','!','#','$','%','&']
num_letter=int(input("Enter number of letters\n"))
# print(num_letter)
num_numbers=int(input("Enter number of numners\n"))
# print(num_numbers)
num_symbols=int(input("Enter number of symbols\n"))
# print(num_symbols)
password=""
for i in range(1,num_letter):
     password+=random.choice(letters)
for j in range(1,num_numbers+1):
     password+=random.choice(numbers)
for k in range(1,num_symbols+1):
     password+=random.choice(symbols)
print(password)     