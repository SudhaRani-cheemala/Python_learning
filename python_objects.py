# class My_Class:
#     x=5
# print(My_Class.x)
# ---------------------------------------------------------------
# class Person:
#     x=100
#     def sample(age,name):
#         print(age,name)
# print(Person.x)        
# Person.sample(6,"sudha")    
# ---------------------------------------------------------------__init__() is like constructor--------
class Animal:
    def __init__(self, name, age):
      self.name = name
      self.age = age
p1 = Animal("Germanshepard", 36)
print(p1.name) 
print(p1.age)