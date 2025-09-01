class Vehicle:
    def __init__(self, type):
        print("The type of vehicle: ", type)


class Car(Vehicle):
    def __init__(self):
        super().__init__("Car")

print(issubclass(Car, Vehicle))
aCar = Car()