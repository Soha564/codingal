class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.pi = 3.14159
    
    def area(self):
        return self.pi * self.radius * self.radius

    def circumference(self):
        return 2 * self.pi * self.radius


radius = float(input("Enter the radius of the circle: "))

my_circle = Circle(radius)


print("Area of the circle:", round(my_circle.area(), 2))
print("Perimeter of the circle:", round(my_circle.circumference(), 2))
