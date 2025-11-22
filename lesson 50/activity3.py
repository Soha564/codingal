def add(num1, num2):
    num3 = num1+num2
    return num3
def minus(num1, num2):
    num3 = num1-num2
    return num3
def multiply(num1, num2):
    num3 = num1*num2
    return num3
def division(num1, num2):
    num3 = num1/num2
    return num3

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

a = add(num1, num2)
print("The sum: ", a)
b = minus(num1, num2)
print("The sum: ", b)
c = multiply(num1, num2)
print("The product: ", c)
d = division(num1, num2)
print("The quotent: ", d)

