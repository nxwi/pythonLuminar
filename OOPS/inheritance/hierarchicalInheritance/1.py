class Shape:
    def color(self, color):
        self.color = color


class Circle(Shape):
    def radius(self, radius):
        self.radius = radius

    def get_area(self):
        print(f"Circle color:{self.color}")
        print(f"Circle area:{3.14 * self.radius ** 2}")


class Square(Shape):
    def side(self, side):
        self.side = side

    def get_area(self):
        print(f"Circle color:{self.color}")
        print(f"Circle area:{self.side ** 2}")


circle = Circle()
circle.color("red")
circle.radius(5)
circle.get_area()

square = Square()
square.color("blue")
square.side(10)
square.get_area()
