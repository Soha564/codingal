string = input("Enter a string:")

print("Direct way to reverse String:", string[::-1])

print("\n ___________________________\n")

reversed_string = ""
for letter in string:
    reversed_string = letter + reversed_string 

print("Reversed string using for loop:", reversed_string)