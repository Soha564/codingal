class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species
    
    def sound(self, sound):
        print(self.name, " makes the sound:", sound)
    
    def display(self):
        print(self.name, "is a good", self.species, "and their age is", self.age)

dog = Animal("Buddy", 4, "Dog")
dog.sound("Barking")
dog.display()

print()

cat = Animal("Sam", 3, "Cat")
cat.sound("Meowing")
cat.display()