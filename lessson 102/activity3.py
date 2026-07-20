string = input("Enter a string:")
vowels = ["a", "e", "i", "o", "u"]
new_string = ""
for i in string:
    if i not in vowels:
        new_string += i
print(new_string)
