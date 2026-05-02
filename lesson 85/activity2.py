def IandJ(A, N, X):
    i = 0
    j = N-1
    while(i<j):
        if(A[i] +A[j] == X):
            return [A[i], A[j]]
        
        elif(A[i] + A[j] < X):
            i += 1

        else:
            j -= 1
        
    return 0
arr  = [2 , 3, 5, 8, 9, 10, 11]
val = (int(input("Enter a number: ")))
print(IandJ(arr, len(arr), val))
