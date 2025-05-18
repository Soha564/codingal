num = int(input("Enter a number:"))
n = int(input("Enter the power of your number:"))

power = 1
for i in range(1, n+1):
    power *= num
    print(power)