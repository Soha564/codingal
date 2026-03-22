def Mean(arr, a_size):
    total = 0
    for i in range(0, a_size):
        total += arr[i]
    return float(total/a_size)
def Median(arr, a_size):
    sorted(arr)
    if a_size % 2 != 0:
        return float(arr[int(((a_size)/2))])
    return float((arr[int(((a_size)/2)-1)]+ arr[int(a_size/2)])*0.5)

arr = [1,2,4,3,5,2]
a_size = len(arr)

print("Mean: ", Mean(arr, a_size))
print("Median: ", Median(arr, a_size))