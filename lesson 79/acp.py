def max_difference(arr):
    if not arr:
        return 0  

    minimum = arr[0]
    maximum = arr[0]

    for num in arr:
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num

    return maximum - minimum
            

arr = [4,5,234,2,6,82,234,5234]
print("Output: ", max_difference(arr))
