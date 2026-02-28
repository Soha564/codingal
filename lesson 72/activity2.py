def arrayTotalSum(a):
    length = len(a)
    if length == 1:
        return a[0]
    
    return a[0] + arrayTotalSum(a[1:])

a = []
i = int(input("Enter a number for length of array: "))
for j in range(i):
    num = int(input("Enter a number for the array: "))
    a.append(num)

print("Array total sum: ", arrayTotalSum(a))