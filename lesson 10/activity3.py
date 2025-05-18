# Print numbers in revers order
# take input: 10
# using for loop print: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
num1 = int(input("Enter a number to reverse:"))
for num in range(num1, 0, -1):
    print(num)