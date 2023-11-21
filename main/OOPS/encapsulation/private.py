class Employee:
    def __init__(self, name, salary):  # public data's
        self.nm = name
        self.__sl = salary

    def __display(self):  # public method
        print(self.nm)
        print(self.__sl)


obj = Employee("John", 10000, )
print(obj.nm)  # public accessing of function

# print(obj.__sal) # private accessing isn't possible
# obj.__display()

print(obj._Employee__sl)
obj._Employee__display()
