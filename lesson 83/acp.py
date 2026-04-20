def Zeroes_at_The_End(a):
    a_size = len(a)
    result = []
    count = 0
    for i in range(a_size):
        if a[i] != 0:
            result.append(i)
        else:
            count += 0
    for j in range(count):
        result.append(0)
    return result
a = [1, 0, 0, 5, 3,2 ,5 ,0, 0, 6,4 ,3, 0, 0]
print(Zeroes_at_The_End(a))