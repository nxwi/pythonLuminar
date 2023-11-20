class A:
    def fun(self):
        print("Hello...")


class B(A):
    def fun(self):
        print("Hai...")


obj = B()
obj.fun()
