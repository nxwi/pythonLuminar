"""
class Maths:
    def add(self, a, b):
        print(a + b)

    def add(self, a, b, c):
        print(a + b + c)


obj = Maths()
obj.add(1, 2, 3)

obj.add(1, 2)
"""

# In the above code, we have defined two add methods,
# but we can only use the second add method, as python
# does not support method overloading directly

from multipledispatch import dispatch


class Maths:
    @dispatch(int, int)
    def add(self, a, b):
        print(a + b)

    @dispatch(int, int, int)
    def add(self, a, b, c):
        print(a + b + c)


obj = Maths()
obj.add(1, 2, 3)
obj.add(1, 2)
