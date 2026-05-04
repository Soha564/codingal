def LargestNbumber(a):
    a_size = len(a)
    for i in range(a_size):
        max_index = i
        for j in range(i+1, a_size):
            if str(a[j]) + str(a[max_index]) > str(a[max_index]) + str(a[j]):
                max_index = j
        
        a[i], a[max_index] = a[max_index], a[i]
    
    return "".join(map(str, a))
a = [ 6, 5, 9, 13, 0, 2, 1]
print(LargestNbumber(a))