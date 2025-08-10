def findmultiple(t):
    multiple = 1
    for i in t:
        multiple *= i
    return multiple

t = (1, 2, 3, 4, 5, 6, 7, 8)
print("Multiple of the tuple:", findmultiple(t))