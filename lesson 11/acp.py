num = int(input("Enter the number: ") ) # 12346
count = 0

while num > 1:
    num = num // 10 # 1234, 123, 12, 1
    count += 1

print("Total digits:", count + 1)
