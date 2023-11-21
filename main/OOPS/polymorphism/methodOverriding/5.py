# Overriding using hybrid-inheritance

class Math:
    def sum(self, a, b):
        print(a / b)


class ChildMath1(Math):
    def sum(self, a, b):
        print(a * b)


class ChildMath2(Math):
    def sum(self, a, b):
        print(a - b)


class SuperChildMath(ChildMath1,ChildMath2):
    def sum(self, a, b):
        print(a + b)


obj = SuperChildMath()
obj.sum(1, 2)
