def OddOccurring(arr):
    res = 0
    for element in arr:
        res = res^element
    return res
arr=[]
n = int(input("Enter array size (must be odd): "))

while (n):
    num = int(input("Enter number: "))
    arr.append(num)
    n-=1

print("\nOdd ocurring number is: ", OddOccurring(arr))