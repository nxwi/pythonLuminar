class A:
    def funa(self):
        print("Parent A")


class B:
    def funb(self):
        print("Parent B")


class C(A, B):
    def func(self):
        print("Child C")


obj = C()
obj.funa()
obj.funb()
obj.func()
