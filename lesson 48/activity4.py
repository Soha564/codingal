num = int(input("Enter a number: "))
if num > 50:
    if num%2 == 0:
        print("The number is greater than fifty and is even.")
    else:
        print("The number is greater than 50 and is odd.")
else:
    print("The numer is less than 50.")