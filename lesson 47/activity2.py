string = input("Enter a string: ")
rev = string[::-1]
if string == rev:
    print("It's a palindrome.")
else:
    print("It's not a palindrome.")