def max_number_of_ones(arr):
    max_count = 0
    count = 0
    for i in arr:
        if i == 1:
            count +=1
            max_count = max(max_count, count)
        else:
            count = 0
    return max_count
arr = [1, 1, 0, 1, 1, 1]
print("Max number of consecutive ones: ", max_number_of_ones(arr))
