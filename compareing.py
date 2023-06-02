def maximun(a,b,c):
    if a>b:
        print("a is greater")
    elif b>c:
        print("b is greater")
    else:
        print("not defined")

a = int(input('a'))
b=int(input('b'))
c=int(input('c'))
print(max(a,b,c))
print(maximun(a,b,c))           
# ------------------------------------------------------printing statements--------------
name = "sars_cov_2"

disease = "covid19"

print("The name of the virus is", name)

print("The name of the virus is {}". format(name))

print("{} is the name of the virus".format(name))

print("the name of the virus is {} & it causes {}".format(name, disease))

print(f"the name of the virus is {name} & it causes {disease}")
#condition

print("the name of virus is" + " "+ name)  
