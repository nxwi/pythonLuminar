# Overriding using hierarchical-inheritance

class Math:
    def sum(self, a, b):
        print(a + b)


class ChildMath1(Math):
    def sum(self, a, b):
        print(a * b)


class ChildMath2(Math):
    def sum(self, a, b):
        print(a - b)


obj = ChildMath1()
obj.sum(1, 2)
obj = ChildMath2()
obj.sum(1, 2)
