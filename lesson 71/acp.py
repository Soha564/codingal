def take_input():
    num = int(input("Enter your number : "))
    
    if num < 0:
        print("Number -ve")
        return
    else:
        print("Number +ve")
        take_input()


take_input()
