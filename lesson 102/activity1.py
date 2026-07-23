string = input("Enter a string:")
new_string = ""
for i in string:
    if i == i.upper():
        new_string += i.lower()
    else:
        new_string += i.upper()
print(new_string)