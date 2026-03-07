def recursiveLength(a):
    if a == []:
        return 0
    
    return 1 + recursiveLength(a[1:])

a = [1,2,3,34,7,5,45,3,2,1,1,1,67,2,3]

length = recursiveLength(a)
print("\nLength of array:", length)