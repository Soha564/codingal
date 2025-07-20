valid = False
while not valid:
    try:
        num = int(input("Enter a number: "))
        if num % 2 == 0:
            print("Bye")
        valid = True

    except ValueError:
        print("Invalid Input (Try Again)")
        