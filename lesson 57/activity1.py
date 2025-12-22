from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def move(self):
        pass
class Human(Animal):
    def move(self):
        print("I can walk and run.")
class Snake(Animal):
    def move(self):
        print("I can slither") 
class Bird(Animal):
    def move(self):
        print("I can fly.")
class Fish(Animal):
    def move(self):
        print("I can swim.")

h = Human()
h.move()

s = Snake()
s.move()

b = Bird()
b.move()

f = Fish()
f.move()