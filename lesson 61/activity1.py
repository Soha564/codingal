# Armstrong numbers
num = int(input("Enter a number: "))
digits = len(str(num))
result = 0
num1 = num
while num1>0:
    digit = num1%10
    result+= digit**digits
    num1//=10

if result == num:
    print(num, "is an armstrong number.")
else:
    print(num, "is not an armstrong number.")