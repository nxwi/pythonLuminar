class Math:
    def sum(self, a, b):
        print(a + b)


class ChildMath(Math):
    def sum(self, a, b):
        print(a * b)


obj = ChildMath()
obj.sum(1, 2)
