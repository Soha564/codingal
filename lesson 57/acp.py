# Parent class
class Shape:
    def area(self):
        pass


# Rectangle child class
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Square child class
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


# MAIN PROGRAM
rect = Rectangle(10, 5)
sq = Square(7)

print("Rectangle area:", rect.area())
print("Square area:", sq.area())

