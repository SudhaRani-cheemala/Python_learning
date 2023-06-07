base=int(input("Enter a base value:"))
exponent=int(input("Enter a exponent value"))
result=1
print(base,"to power",exponent,"=",end= '')
for exponent in range(exponent,0,-1):
    result*=base
print(result)    