# Create a function length

from multipledispatch import dispatch


class Length:
    @dispatch(str)
    def str(self, x):
        n = 0
        for i in x:
            n += 1
        print(n)

    @dispatch(list)
    def list(self, x):
        n = 0
        for i in x:
            n += 1
        print(n)

    @dispatch(set)
    def set(self, x):
        n = 0
        for i in x:
            n += 1
        print(n)

    @dispatch(dict)
    def dict(self, x):
        n = 0
        for i in x:
            n += 1
        print(n)

    @dispatch(tuple)
    def tuple(self, x):
        n = 0
        for i in x:
            n += 1
        print(n)


obj = Length()
obj.str('abc')
obj.list([1, 2, 3, 4, 5])
obj.set({'a', 'b'})
obj.dict({'name': 'alex', 'age': 22})
obj.tuple(('a', 'b', 'c'))
