num = int(input("Enter a number: "))
num3 = " "
while num > 0:
    num3 = str(num%2) + num3
    num = num//2
print(num3)