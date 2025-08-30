# Write a program to create a dog class, create a class variable animal and inside the constructor, create another two variables - breed and colour inside the constructor. Next up, create two different objects for different breeds of dogs. Also, display the details of both breeds of dogs.
class Animal:
    def __init__(self, breed, colour):
        self.breed = breed
        self.colour = colour

    def extra(self, height, weight):
        self.height = height
        self.weight = weight
    
    def display(self):
        print("This dog is a ", self.breed, " and is the colour ", self.colour, ". They weigh ", self.weight, " and have a height of ", self.height, ".")

dog1 = Animal("Chihuahua", "brown")
dog1.extra("17cm", "2.6kg")
dog1.display()

print()

dog2 = Animal("Great Dane","black")
dog2.extra("86 cm", "79kg")
dog2.display()

