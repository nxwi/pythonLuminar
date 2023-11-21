# Overriding using multiple-inheritance

class Math1:
    def mult(self, a, b):
        print(a * b)


class Math2:
    def sum(self, a, b):
        print(a + b)


class ChildMath(Math1, Math2):
    def mult(self, a, b):
        print(a - b)

    def sum(self, a, b):
        print(a - b)


obj = ChildMath()
obj.mult(1, 2)
obj.sum(1, 2)
