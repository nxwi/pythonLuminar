class Shape:
    def __init__(self, color):
        self.color = color


class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def get_area(self):
        print(f"Circle color:{self.color}\nCircle area:{3.14 * self.radius ** 2}")


class Square(Shape):
    def __init__(self, color, side):
        super().__init__(color)
        self.side = side

    def get_area(self):
        print(f"Circle color:{self.color}\nCircle area:{self.side ** 2}")


circle = Circle("red", 5)
circle.get_area()

square = Square("blue", 10)
square.get_area()
