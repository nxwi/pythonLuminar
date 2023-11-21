# Create a function product


from multipledispatch import dispatch


class Maths:
    @dispatch(int, int)
    def product(self, a, b):
        print(a * b)

    @dispatch(int, int, int)
    def product(self, a, b, c):
        print(a * b * c)

    @dispatch(float, float)
    def product(self, a, b):
        print(a * b)

    @dispatch(float, float, float)
    def product(self, a, b, c):
        print(a * b * c)


obj = Maths()
obj.product(1, 2)
obj.product(1, 2, 3)
obj.product(1.2, 3.3)
obj.product(1.2, 2.2, 3.3)
