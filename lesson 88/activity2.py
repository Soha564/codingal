def OneSwapChecker(a):
    a_size = len(a)
    a2 = a.sort
    for i in range(a_size):
        for j in range(i+1, a_size):
            arr = a.copy()
            arr[i],arr[j] = arr[j], arr[i]
            if arr == a2:
                return True
    return False
a = [1, 2, 3, 7, 9, 6]
result = OneSwapChecker(a)
if result:
    print("One swap needed.")
else:
    print("More than one swap needed.")