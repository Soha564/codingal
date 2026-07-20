string = input("Enter a string:")
new_string = ""
for i in string:
    if i >=chr(ord("a")):
        new_string += chr(ord(i) - 32)
    else:
        new_string += chr(ord(i) + 32)

print(new_string)