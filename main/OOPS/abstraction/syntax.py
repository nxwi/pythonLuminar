from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def reg_num(self):
        pass

    @abstractmethod
    def color(self):
        pass

    @abstractmethod
    def owner(self):
        pass

    @abstractmethod
    def fuel(self):
        pass


class Car(Vehicle):

    def reg_num(self):
        print("007")

    def color(self):
        print("Black")

    def owner(self):
        print("John")

    def fuel(self):
        print("Petrol")

    def sunroof(self):
        print("Car have sunroof")


obj = Car()
obj.sunroof()
