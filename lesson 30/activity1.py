# Write a program to create a class with following variables and methods - 1. Private variable named privateVar that contains an integer value 2. Create a private function privMeth that prints a message 3. Create a function hello that prints the value of privateVar 4. Create an object for the class and call all the functions.

class MakePrivate:
    __privateVar = 200

    def __privMeth(self):
        print("This is a prived method.")

    def hello(self):
        print("Hello, the private variable value is: ", self.__privateVar)

ob = MakePrivate()
# print(ob.privateVar) = will show attribute error
# ob.__privMeth() - will show attribute error
ob.hello()
