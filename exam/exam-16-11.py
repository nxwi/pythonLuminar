# 1. Create a class vehicle without any variables and methods ?

"""
class Vehicle:
    pass
"""

# 2. Create a parent class vehicle with child classes: bus, car , bike the child classes should access the properties
# and behaviour of parent class finally create a bus object, a car object and a bike object ? (using constructor)

"""
class Vehicle:
    def __init__(self, reg_no, color):
        self.reg_no = reg_no
        self.color = color


class Bus(Vehicle):
    def __init__(self, passengers, reg_no, color):
        super().__init__(reg_no, color)
        self.passengers = passengers

    def display(self):
        print(f"Registration Number: {self.reg_no}")
        print(f"Color: {self.color}")
        print(f"Number of Passengers: {self.passengers}")


class Car(Vehicle):
    def __init__(self, transmission, reg_no, color):
        super().__init__(reg_no, color)
        self.transmission = transmission

    def display(self):
        print(f"Registration Number: {self.reg_no}")
        print(f"Color: {self.color}")
        print(f"Transmission: {self.transmission}")


class Bike(Vehicle):
    def __init__(self, cc, reg_no, color):
        super().__init__(reg_no, color)
        self.cc = cc

    def display(self):
        print(f"Registration Number: {self.reg_no}")
        print(f"Color: {self.color}")
        print(f"Engine Capacity: {self.cc}cc")


bus = Bus(50, "KL-1234", "Yellow")
bus.display()

car = Car("Automatic", "KL-5678", "Red")
car.display()

bike = Bike(150, "KL-9012", "Black")
bike.display()
"""

# 3. What does the super() do in python ?

"""
super() is used to call methods of the parent class from within a subclass
"""

# 4. What is a member function, and another name for member function ?

"""
It is a function that is defined within a class and can access the class's attributes and methods.
Also called method or function.
"""

# 5. Explain the diff between multiple inheritance and single inheritance with example code ?

"""
-> Single inheritance: child class that inherits from a single parent class.

class Shape:
    def __init__(self, color):
        self.color = color


class Square(Shape):
    def __init__(self, side, color):
        super().__init__(color)
        self.side = side

    def display(self):
        print(self.color)
        print(self.side * self.side)


square = Square(5, "Blue")
square.display()

-> Multiple inheritance: a single child inherits properties of multiple parents.

class Shape:
    def __init__(self, color):
        self.color = color


class Colorable:
    def change_color(self, color):
        self.color = color


class Square(Shape, Colorable):
    def __init__(self, side, color):
        super().__init__(color)
        self.side = side

    def display(self):
        print(f"Color: {self.color}")
        print(f"Side: {self.side}")
        print(f"Area: {self.side * self.side}")


square = Square(5, "Blue")
square.display()
square.change_color("Red")
square.display()
"""

# 6. What is static variable ? explain with example ? (inheritance)

"""
A variable that has constant value during the program execution which is defined inside a class and outside a function
"""
