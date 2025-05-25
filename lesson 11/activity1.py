# Write a program to find the sum of natural numbers.
nth = int(input("Enter the nth number: "))

i = 1
sum = 0
10

while i <= nth:
    print(i)
    sum = sum + i
    i = i + 1

print(f"sum of {nth} natural numbers is: {sum}")