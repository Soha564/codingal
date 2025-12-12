class student:
    grade = 9
    name = "Penguin"

    def intro(self):
        print("Hi i am a student.")
    
    def details(self):
        print("My name is ", self.name)
        print("I study in grade ", self.grade)

ob = student()
ob.intro()
ob.details()
