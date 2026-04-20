def  SubArraySum(a, sum):
    a_size = len(a)
    for i in range(a_size):
        count = 0
        for j in range(i, a_size):
            count += a[j]
            if count == sum:
                return a[i], a[j]
    return -1
a = [1, 2, 3, 4, 7, 4, 89, 9, 7]
print(a)
sum = int(input("Enter a number for a sum of a subarray in the array: "))
print(SubArraySum(a, sum))
        