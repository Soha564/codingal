def printOneToTen(n):
    if n>10:
        return 
    print(n)
    printOneToTen(n+1)

print(printOneToTen(1))