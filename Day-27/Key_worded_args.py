def calculate(n,**kwargs):
  print(kwargs)
#   for key,value in kwargs.items():
#       print(key)
#       print(value)
  n+=kwargs["add"]
  n*=kwargs["multiply"]
calculate(2,add=3,multiply=5)  
class Car:
    def __init__(self,**kw) :
        # self.make=kw["make"]
        # self.model=kw["model"]
        self.make=kw.get("make")
        self.model=kw.get("model")
        self.colour=kw.get("colour")
        self.seats=kw.get("seats")
my_car=Car(make="Nissan",model="GT-R")
print(my_car.model)    
def test(*args):
    print(args)
 
test(1,2,3,5)    
     