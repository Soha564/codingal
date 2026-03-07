def checkPowerOfFour(n):
    if n == 1:
        return True
    if n < 1 or n%4 != 0:
        return False
    return checkPowerOfFour(n//4)
n = int(input("Enter a number: "))
if checkPowerOfFour(n):
    print(n, "is a power of four.")
else:
    print(n, "isnt a power of four.-")