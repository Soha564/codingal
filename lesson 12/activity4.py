# Write a program to print all the prime numbers which come in the range entered by the user?
low = int(input("Enter the lowest number: "))
high = int(input("Enter the highest number: "))

while low <= high:
    if low <= 1:
        factor = 2

        while factor < low:
            if low % factor == 0:
               break
            factor += 1
        else:
            print(low)
    low += 1
