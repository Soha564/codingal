def rotations(a, n, a_size):
    for i in range(n):
        rotate(a, a_size)
def rotate(a, a_size):
    temp = a[0]
    for i in range(a_size - 1):
        a[i] = a[i + 1]
    a[a_size - 1] = temp
def printArray(a, a_size):
    for i in range(a_size):
        print(a[i])
    print("\n")
a = [213,214,121,143,2145,12342,214]
n = int(input("Enter a number: "))
a_size = len(a)
printArray(a, a_size)
rotations(a, n, a_size)
printArray(a, a_size)