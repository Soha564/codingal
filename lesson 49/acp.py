# Armstorng numbers
# E.g 370 = 3^3 + 7^3 + 0^3
# Program to check Armstrong number using loops only

num1 = int(input("Enter a number: "))
num2 = num1
n = 0

while num2 > 0:
    num2 //= 10
    n += 1

num2 = num1
sum_of_powers = 0

while num2 > 0:
    digit = num2 % 10
    sum_of_powers += digit ** n
    num2 //= 10
    
if sum_of_powers == num1:
    print(num1, "is an Armstrong number.")
else:
    print(num1, "is not an Armstrong number.")
