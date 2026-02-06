num = int(input("Enter a number: "))
position = int(input("Enter a position: "))
result = num & ~(1<<position)
print(result)