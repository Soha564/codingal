# Write a program to create a class Point that consists of a constructor to set coordinates equal to x and y. Also, it consists of a function that returns the coordinates in Point format. Create an object passing the coordinates and print the Point.

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    # Method to print points in the coordinate format
    def __str__(self):
        return "({}, {})".format(self.x, self.y)
    
# Create an object
p1 = Point(2, 3)
print(p1) # when printing object __str__ method is called upon

p2 = Point()
print(p2) # - " "

# Using Len
class LenExample:
    def __init__(self, text):
        self.text = text
    
    def __len__(self):
        return len(self.text)
    
l = LenExample("Python")
print(len(l))