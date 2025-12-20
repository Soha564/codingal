class person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def display(self):
        print(self.fname, self.lname)

class student(person):
    def __init__(self, fname, lname, year):
        self.year = year

        super().__init__(fname, lname)

obj = student("John", "Joseph", 1967)

obj.display()
print(obj.year)