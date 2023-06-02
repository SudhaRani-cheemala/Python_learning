def text_print():
    print("Hello")
text_print()    
# ---------------------------------------------wehn we not mention return statement you will get None------------------------------
def call(x,y):
    sum=x+y
    print(sum)
    # return sum
z=call(10,20)
print(z)
# -----------------------------------------------list,tuple,dictionary-------------
def list_print(list1):
    for i in list1:
        print(i)
c_list=["eclairs","jelly","alphelibe"]        
list_print(c_list)        
# -----------------------------------------------------------------------------
def fun1():
    print("iam function1")
    fun2()
def fun2():
    print("iam function 2")
fun1()
fun2()
# -----------------------------------------
def string_reverse(str1):
    rstr1 = ''
    index = len(str1)
    while index > 0:
        rstr1 += str1[ index - 1 ]
        index = index - 1
    return rstr1
print(string_reverse('1234abcd'))
#------------------------------------------------------ 
#  Write a Python function to multiply all the numbers in a list.
# Sample List : (8, 2, 3, -1, 7)
# Expected Output : -336
def multiply(numbers):  
    total = 1
    for x in numbers:
        total *= x  
    return total  
print(multiply((8, 2, 3, -1, 7)))
# ----------------------------------------------------------inserting string within string--------------
string1="Hello i like %s" %"python"
print(string1)
# --------------------------------Inserting integer within a string----------------
my_string="%i + %i= %i" % (1,2,4)
print(my_string)
# --------------Inserting float within a string-------------------
string="%f" %(1.89)
print(string)
string2="%.2f" %(1.6666)
print(string2)
# Operators--------------------------------------------------------------------------
# Arithmetic Operator--------------------------------------------- 
print(12.4/2)
print(5.5/4.5)
# floor division--
print(5.5//4.5)
print(6.2//3.5)
# Modulo----------------------------------
print(10%3)
# precedence-------------
print(10-3*4)
# ------------paranthesis------------
print((10-3)*5)
#--------------------------------- Comparison Operator----------------------------
# the result of a comparison is always boolean
num1=10
num2=5
if num1>num2:
 print("Greater")
def summation(a,b):
    sum1=a+b
    return sum1
z=summation(10,20)
print(z) 

# -----------------------------------Assignment Operators-----------------------------------------
num = 10
print(num)

num += 5
print(num)

num -= 5
print(num)

num *= 2
print(num)

num /= 2
print(num)

num **= 2
print(num)
# ----------------------------Logical opetrator--------------------------------True as 1 and false as 0
my_bool=True or False
print(my_bool)
my_bool1=True and False
print(my_bool1)
print(not my_bool1)
# -------------------------------Bitwise operator---------------------------&,|,~,^<<,>>
num = 63

if num >= 0 and num <= 100:
    if num >= 50 and num <= 75:
        if num >= 60 and num <= 70:
            print("The number is in the 60-70 range")
# --------------if condition---------------------------
num=10
if num>=5:
    num=20
    new_num=num*5
print(num) 
print(new_num)   
# ---------------------ELIF---------------------------
light = "Red"

if light == "Green":
    print("Go")

elif light == "Yellow":
    print("Caution")

elif light == "Red":
    print("Stop")

else:
    print("Incorrect light signal")

# def func():
#     name = "Stark"
#     return name
# func()
# print(name)
# -------------------String operstors--------------------str.find("substring",start,end)
sample_str="This is my tab"
print(sample_str.find("is"))
print(sample_str.find("is",2,9))
# -----------------------Replace------------------------str.replace("substring_to_be_replaced",new_string)
print(sample_str.replace("is","hello"))
print(sample_str.upper())
print(sample_str.lower())
# ----------------------------------Joining string----------------------------------------------------------
list3=["a","b","c"]
print('>>'.join(list3))
print('<<'.join(list3))
print(','.join(list3))
# -----------formatting strings-----------------------
str2="Hello iam {learing}  at {hello}".format(learing="python",hello="home")
print(str2)
str3="learn {0} at {1}".format("python","home")
print(str3)
str4="learn {} at {}".format("python","home")
print(str4)
#------------------------------ type conversion---------------------
# string to integer
print(int("12"))

# print (int("Hello")) # This wouldn't work! 
# characters into unicode values
print(ord('a'))
# float conversion
print(float(24))
print(float('24.8'))
print(float(True))
print(float(False))
# string conversion
print(str(12))
print(str(True))
print(str(233.90))
# Bool conversion
print(bool(10))
print(bool(""))
print(bool("dafaf"))
print(bool("0.0"))
print(bool(None))
#------------------------ Functions in functions---------------------
def add(a1,b1):
    c1=a1+b1
    return c1
def sub(a1,b1):
    c1=a1-b1
    return c1
def cal(operation,a1,b1):
    return operation(a1,b1)
result=cal(add,10,30)
print(result)    
result=cal(sub,10,90)
print(result)