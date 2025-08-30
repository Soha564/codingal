# Write a program to create a class with the name Student and perform the following tasks - 1. Declare a variable grade 2. Print a sentence inside the class 3. Create an object of class student and see the output

class Student:
    # attribute
    grade = 8

    # method
    def display(self):
        print("Welcome, the student of grade", self.grade)

# create object/inastance
student1 = Student()
print("Grade:", student1.grade)
student1.display() 