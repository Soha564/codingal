# Write a program to create a base class that consists of two functions - one to display a value, and another function is an abstract method. Next, create a subclass that consists of a method similar to the abstract method. Finally, showcase how Abstraction is being implemented in this example.

from abc import ABC, abstractmethod

class MyAbstractClass(ABC):
    def print(self, x):
        print("Passed value", x)

    @abstractmethod
    def task(self):
        pass
class TestClass(MyAbstractClass):
    def task(self):
        print("We are inside the child class's task method.")


t = TestClass()
t.task()
t.print(299)