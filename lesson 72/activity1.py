def checkSorted(a):
    length = len(a)
    if length == 1 or length == 0:
        return True
    
    return a[0] <= a[1] and checkSorted(a[1:])

a = []
i = int(input("Enter a number for length of array: "))
for j in range(i):
    num = int(input("Enter a number for the array: "))
    a.append(num)

if checkSorted(a):
    print("\nYes, given array is sorted.")
else:
    print("\nNo, given array is not sorted.")