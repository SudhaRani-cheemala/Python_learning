class Base:
    def __init__(self):
        # protecetd variable with single underscore '_' can be accessd in own calss and derived class
        self._a=10
        self.__b=20
        print(self.__b)    
class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print(self._a)
        # this double underscore variable cannot be accessed outside the class even in derived class also
        print(self.__b)
ob1=Base()
ob2=Derived()        