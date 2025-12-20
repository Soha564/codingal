class employer:
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print("Name is", self.name)
        print("ID Number is", self.idnumber)

class employee(employer):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.pot = post

        super().__init__(name, idnumber)

obj = employee("Joseph", 67, "£2000", "Assistant Head")

obj.display()