# Write a Python program to create two classes - BMW and Ferrari with similar methods and implement Polymorphism on them.

class BMW:
    def fuel_type(self):
        print("BMW uses gasoline")

    def max_speed(self):
        print("BMW's max speed is 190mph.")


class Ferrari:
    def fuel_type(self):
        print("Ferrari uses gasoline")

    def max_speed(self):
        print("Ferrari's max speed is 217mph.")

b = BMW()
f = Ferrari()

# Polymorphism
cars = (b, f)

for car in cars:
    print("\n----------------------------------\n")
    car.fuel_type()
    car.max_speed()
    print("\n----------------------------------\n")
