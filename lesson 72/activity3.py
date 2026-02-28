def checkLargestValue(a):
    length = len(a)
    if length == 1 or length == 0:
        return a[0]
    max_val = checkLargestValue(a[1:])
    
    return max(a[0], checkLargestValue(a[1:]))

a = []
i = int(input("Enter a number for length of array: "))
for j in range(i):
    num = int(input("Enter a number for the array: "))
    a.append(num)

print("Largest element of array: ", checkLargestValue(a))