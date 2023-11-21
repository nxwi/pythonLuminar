class Parent:
    def funa(self):
        print("Parent")


class A(Parent):
    def funb(self):
        print("Derived A")


class B(Parent):
    def func(self):
        print("Derived B")


obj1 = A()
obj1.funa()
obj1.funb()

obj2 = B()
obj2.funa()
obj2.func()
