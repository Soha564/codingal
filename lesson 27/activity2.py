# Write a program to create a class Vehicle and perform the following tasks - 1. Create an __init__ method with arguments - max_speed and mileage 2. Create an object of class Vehicle and pass the maximum speed and mileage of the car 3. Print the values of max_speed and mileage by using the object

class Vehicle:
    # constructor
    def __init__(self, max_speed, mileage):
        # initialising
        # instance variables
        self.max_speed = max_speed
        self.mileage = mileage
        
car = Vehicle(150, 24)
van = Vehicle(240, 56)

print("The car's max speed:", car.max_speed)
print("The car's mileage:", car.mileage)

print()

print("The van's max speed:", van.max_speed)
print("The van's mileage:", van.mileage)