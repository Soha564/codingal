# Write a Python program to generate a random password consisting of lower case and upper case characters along with numbers. You can also use random module for shuffling the password generated.
import random

def generate_password():
    print("Simple Password Generator")

    length = int(input("Enter desired password length (minimum 6): "))
    if length < 6:
        print("Password too short. Try again.")
        return

    include_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    include_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    include_digits = input("Include numbers? (y/n): ").lower() == 'y'
    include_charc = input("Include special characters? (y/n): ").lower() == 'y'

    upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_letters = 'abcdefghijklmnopqrstuvwxyz'
    digits = '0123456789'
    special_charc = '!£$%^&*():@@~<>?;#,./}{][_+-=|'

    char_pool = ''
    if include_upper:
        char_pool += upper_letters
    if include_lower:
        char_pool += lower_letters
    if include_digits:
        char_pool += digits
    if include_charc:
        char_pool += special_charc

    if char_pool == '':
        print("You must choose at least one character type.")
        return
    password = []
    for i in range(length):
        password.append(random.choice(char_pool))

    random.shuffle(password)

    print(" Your password is: ", end="")
    for i in password:
        print(i, end="")
    print()
 

generate_password()
