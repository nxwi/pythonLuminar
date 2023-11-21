# Create an abstract class with abstract functions using arguments,
# at least two child class and three abstract methods required

from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def reg_num(self, reg_num):
        pass

    @abstractmethod
    def color(self, color):
        pass

    @abstractmethod
    def owner(self, owner):
        pass


class Car(Vehicle):

    def reg_num(self, reg_num):
        print(reg_num)

    def color(self, color):
        print(color)

    def owner(self, owner):
        print(owner)

    def sunroof(self):
        print("Car have sunroof")


class Bus(Vehicle):

    def reg_num(self, reg_num):
        print(reg_num)

    def color(self, color):
        print(color)

    def owner(self, owner):
        print(owner)

    def low_floor(self):
        print("It is low floor")


obj1 = Car()
obj1.reg_num(101)
obj1.color("Black")
obj1.owner("John")
obj1.sunroof()

obj2 = Bus()
obj2.reg_num(102)
obj2.color("White")
obj2.owner("Sam")
obj2.low_floor()
