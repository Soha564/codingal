num = int(input("Enter number: "))

position = 1

while num > 0:
    if num & 1:
        break
    num >>= 1
    position += 1

print("Position of the first set bit:", position)
