def SecondLargest(a, a_size):
    largest- second_largest = -2937485
    for i in range(a_size):
        if (a[i] > largest):
            second_largest = second_largest
            largest = a[i]
        elif (a[i]> second_largest and a[i] != largest):
            second_largest = a[i]

    print(second_largest)

a = [23,56,23453,123245,2134,2345,1234,24356]
a_size = len(a)
SecondLargest(a, a_size)