# Write a program to implement abstraction on animal class (base class). The abstract method will be move will display what subclasses can do. Subclasses can be something like - Human, Dog.

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def move(self):
        pass


class Dog(Animal):
    def move(self):
        print("I can walk.")

class Snake(Animal):
    def move(self):
        print("I can slither.")

class Fish(Animal):
    def move(self):
        print("I can swim.")

class Bird(Animal):
    def move(self):
        print("I can fly.")

d = Dog()
d.move()

s = Snake()
s.move()

f = Fish()
f.move()

b = Bird()
b.move()