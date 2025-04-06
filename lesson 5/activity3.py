# Write a program to check whether the given number is greater than 15 or smaller than 15.

num = int(input("Please enter a number:"))

if num > 15:
    print(num, "is greater than 15.")
elif num == 15:
    print(num, "is equal to 15.")
else:
    print(num, "is less than 15")