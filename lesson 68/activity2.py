num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
count = 0
while num1 >= num2:
    num1 = num1 - num2
    count +=1

print("num1 divided by num2 equals ", count)