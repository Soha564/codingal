# Write a program to find the factorial using recursive function
# E.g 4 factorial = 4! = 4 * (4-1) * (4-2) * (4-3) = 4 * 3 * 2 * 1 = 24

def factorial(num):
    if num == 0 or num == 1:
        return 1
    
    return num * factorial(num - 1)

user_input = int(input("Can you enter a number to factorialise?"))

print(factorial(user_input))
