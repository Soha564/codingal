# Write a Python program to implement Inheritance by creating a Parent Class Vehicle with a constructor that has details like name, maximum speed, and mileage. Then, create a Child Class Bus that inherits Class Vehicle. Finally, showcase Inheritance to display the details of the Vehicle Bus named - School Volvo.

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

# child class
class Bus(Vehicle):
    pass

# ALWAYS CREATE THE OBJECT OF THE CHILD CLASS
schl_bus = Bus("School Volvo", 180, 12)
print(f"Name: {schl_bus.name} \nSpeed: {schl_bus.max_speed} \nMileage {schl_bus.mileage}")