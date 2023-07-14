class Parent1():
    def parent1(self,age,name):
        self.age=age
        self.name=name
        print("the name of the Parent1 is {}".format(self.name))
        print("the age of the Parent1 is {}".format(self.age))
class Parent2():
        def parent2(self,age,name):
            self.age=age
            self.name=name
            print("the name of the Parent1 is {}".format(self.name))
            print("the age of the Parent1 is {}".format(self.age))   
class Child(Parent1,Parent2):
        def child(self,age,name):
            self.age=age
            self.name=name
            print("the name of the Child is {}".format(self.name))
            print("the age of the Child is {}".format(self.age))   
c1=Child()
c1.parent1(10,"manoj")
c1.parent2(20,"sana")
c1.child(30,"sameer")            
                          