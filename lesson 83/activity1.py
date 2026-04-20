def linear_search(a, z):
    a_size = len(a)
    for i in range(a_size):
        if a[i] == z:
            return i
    return -1
a = [ 1,2,143,4,24,3,67,1,1,3]
z = int(input("Enter a number:"))
print(linear_search(a, z))