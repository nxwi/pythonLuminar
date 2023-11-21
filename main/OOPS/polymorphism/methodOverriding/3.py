# Overriding using multilevel-inheritance

class Math:
    def sum(self, a, b):
        print(a + b)


class ChildMath(Math):
    def sum(self, a, b):
        print(a * b)


class SuperChildMath(ChildMath):
    def sum(self, a, b):
        print(a - b)


obj = SuperChildMath()
obj.sum(1, 2)
