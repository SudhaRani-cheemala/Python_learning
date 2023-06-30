# Python OOPS concept
# car=CarBluePrint()
# here car is an Object and CarBluePrint is a class name which acts as a construction 
# import another_module
# print(another_module.another_variable)
# import turtle
# timmy=turtle.Turtle()
from turtle import Turtle,Screen
tim=Turtle()
tim.shape("turtle")
tim.color("red")
tim.left(100)

# Object Attributes
# for example car has attributes like speed,fuel
# accessing the attributes is like if car is an object car.speed,car.fuel we can access
my_screen=Screen()
print(my_screen.canvwidth)
print(my_screen.canvheight)
# Object Methods
# here car.stop() means car is and object by object calling a method called stop()
# exitonclick() this function will exit by clicking on screen
my_screen.exitonclick()
# Python Packages:
# pypi python package index
from prettytable import PrettyTable
table=PrettyTable()
table.add_column("Pokeman Name",["Pickchu","Sqrtirets","Charmder"])
table.add_column("Type",["Electric","Water","Fire"])
table.align="r"
print(table)