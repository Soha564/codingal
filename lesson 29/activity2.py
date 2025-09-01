# Write a program to create a parent class Person (attributes - name, id number) with a method display to display the attributes. Next, create a child class Employee (attributes - name, id number, salary, post). Access the attributes of parent class in child class. Then, create an object for child class and call the display method to display the name and id number.

class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display(self):
        print(f"Name: {self.name}, ID: {self.id}" )

class Employee(Person):
    def __init__(self, name, id, salary, post):
        Person.__init__(self, name, id)
        self.salary = salary
        self.post = post

employee1 = Employee("John Doe", 233, 500.50, "Executive")
employee1.display()
