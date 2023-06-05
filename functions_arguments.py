def sample(a,b):
    c=a+b
    return c
res=sample(10,30)
print(res)    
# -----------------------------------------
def show_display(name,salary=9000):
    print("Name:" , name,"salary:" ,salary)
show_display("Ben",12000)
show_display("Hannah")
show_display("Smith",98777)
# # ---------------------------------------------------
def out_fun(a,b):
    def inn_fu(a,b):
        sum=a+b
        return sum
    res=inn_fu(a,b)
    return res+5
    print(res)    
result=out_fun(10,50)  
print(result)  
# ---------------------------------------------------------assign existing function name to new name 
def display_name(name,age):
    return name,age
res1=display_name("Smith",56)
print(res1)
# -------------------------------------------------list of even numbers---------------------------------
def list_of():
    print(tuple(range(4,30,2)))
    print(list(range(4,30,2)))
    print(set(range(4,30,2)))
    print(max(range(4,30,2)))
    print(min(range(3,30,3)))
list_of()    
# -------------------------------
def add(a, b):
    return a+5, b+5

result = add(3, 2)
print(result)
# ====================================
def fun1(name, age=20):
    print(name, age)

fun1('Emma', 25)
# =========================
def outer_fun(a, b):
    def inner_fun(c, d):
        return c + d

    return inner_fun(a, b)
    return a

result = outer_fun(5, 10)
print(result)
# ----------------------------------------------------
def add(*args):
    print(args,type(args))
add(10,20)
#-----------------------------------------------------
def number_args(*numbers):
      total=0
      for num in numbers:
            total+=num
      return total
print(number_args(10,20))      
print(number_args(10,20,30))
print(number_args(10,90,80,70))
# -----------------------------------------------------------------------
def fruits(**kwargs):
    print(kwargs,type(kwargs))
fruits(hello=5,hell="hello")    

