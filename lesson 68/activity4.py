num = int(input("Enter a number: "))
position = int(input("Enter a position: "))
num>>=position
num = (num^1)
num<<=position
print(num)