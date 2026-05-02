def TwoSum(a, num):
    a_size = len(a)
    for i in range(a_size):
        for j in range(i+1, a_size):
            if a[i] + a[j] == num:
                return a[i], a[j]
    return -1
a = [1 ,2 , 3, 4, 5, 6, 7, 8]
num = int(input("Enter a number: "))
print(TwoSum(a, num))            