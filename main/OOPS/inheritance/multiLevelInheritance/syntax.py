class A:
    def funa(self):
        print("Parent A")


class B(A):
    def funb(self):
        print("Derived B")


class C(B):
    def func(self):
        print("Derived C")


obj = C()
obj.funa()
obj.funb()
obj.func()
