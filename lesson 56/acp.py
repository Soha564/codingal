class rectangle:
    def __init__(self, angle, four_sides):
        self.angle = angle
        self.four_sides = four_sides

    def display(self):
        print("Four sides: ", self.four_sides)
        print("Angles: ", self.angle)
class square(rectangle):
    def __init__(self, name, angle, four_sides):
        self.name = name

        super().__init__(angle, four_sides)

obj = square("Square", 90, True)

obj.display()