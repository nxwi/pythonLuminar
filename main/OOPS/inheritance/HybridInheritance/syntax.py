class Parent:
    def parentfun(self):
        print("Parent class")


class Derived1(Parent):
    def derivedfun1(self):
        print("Derived class 1")


class Derived2(Parent):
    def derivedfun2(self):
        print("Derived class 2")


class Derived3(Derived1, Derived2):
    def derivedfun3(self):
        print("Derived class 3")


obj = Derived3()
obj.parentfun()
obj.derivedfun1()
obj.derivedfun2()
obj.derivedfun3()
