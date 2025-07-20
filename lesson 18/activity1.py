try:
    number = int(input("Enter a number: "))
    print("Number is:", number)
except ValueError as exp:
    print("The error is: ", exp)  