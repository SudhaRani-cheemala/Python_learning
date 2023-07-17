# poly means many in which all the methods have same name
class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("Drive!")
class Boat:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("Sailing the boat")
class Bike:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("Ridning bike") 
car1=Car("Ford","Classic")
boat=Boat("Ibiaz","Claasic")
bike=Bike("Boeing_bike","classic")
for x in (car1,boat,bike):
    x.move()
                                  

