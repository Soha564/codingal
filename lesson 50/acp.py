# Fibonacci
def fibonacci(n, a, b):
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        return fibonacci(n-1, a, b) + fibonacci(n-2, a, b)

def print_fibonacci_sequence(terms, a, b):
    print("Fibonacci sequence:")
    for i in range(terms):
        print(fibonacci(i, a, b), end=" ")

first = int(input("Enter the first digit: "))
second = int(input("Enter the second digit: "))
terms = int(input("Enter how many terms you want: "))

print_fibonacci_sequence(terms, first, second)
