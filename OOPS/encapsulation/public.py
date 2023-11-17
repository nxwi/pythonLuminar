class Employee:
    def __init__(self, name, salary, phone):  # public data's
        self.nm = name
        self.sl = salary
        self.ph = phone

    def display(self):  # public method
        print(self.sl)
        print(self.ph)
        print(self.nm)


obj = Employee("John", 10000, 9876543)
obj.display()  # public accessing of function
print(obj.nm)  # public accessing of variables
print(obj.sl)
print(obj.ph)
