class Grandfaher():
    def grand_fun(self,name):
        self.name=name
        print("Grandfather name is {}".format(self.name))
class Father(Grandfaher):
    def father_fun(self,name):
        self.name=name
        print("father name is {}".format(self.name))
class Son(Father):
    def son_fun(self,name):
        self.name=name
        print("son name is{}".format(self.name))
g1=Grandfaher()
f1=Father()
s1=Son()
s1.grand_fun("Smith")