def SetOrNot(num, n):
    if num&(1<<(n-1)):
        print("\nSET")
    else:
        print("\nNOT SET")

num = int(input("Enter a number: "))
n = int(input("Enter a bit number: "))
SetOrNot(num, n)