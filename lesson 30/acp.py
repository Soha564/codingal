# Create a class reverse that consists of a constructor with a default value of string s. Then, create a method that will return the reversed string. The value of string s must be equal to the word taken as input from the user.

class Reverse:
    def __init__(self, s = ""):
        self.s = s
    def reversing(self):
        reversed_string = ""
        word = ""
        for char in self.s:
            if char != " ":
                word += char
            else:
                reversed_sentence += word[::-1]
                word = ""
        reversed_string += word[::-1]       
        return self.s[::-1]
    
user_input = input("Enter a string: ")
reverse = Reverse(user_input)
print("Rewritten string: ", reverse.reversing())
