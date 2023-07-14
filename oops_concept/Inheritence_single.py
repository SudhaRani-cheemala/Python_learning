# single and multiple inheritence
class Parent():
    def parent_fun(self,age,name):
        self.age=age
        self.name=name
        print("the name of the parent is {}".format(self.name))
        print("the age of the parent is{}".format(self.age))
class Child1(Parent):
    def child_fun(self,age,name):
        self.age=age
        self.name=name
        print("The name of the person is {}".format(self.name))    
        print("the age of the parent is{}".format(self.age))
class Child2(Parent):
    def child1_fun(self,age,name):
        self.age=age
        self.name=name
        print("The age of the child2 is {}".format(self.name))    
        print("The age of the child2 is {}".format(self.age))           
p1=Parent()
p1.parent_fun(10,"sumanth")        
p2=Child1()
p2.parent_fun(20,"salma")
p2.child_fun(30,"suma")
p3=Child2()
p3.child1_fun(40,"chandra")
p3.child1_fun(69,"RGV")

