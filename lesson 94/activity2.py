def left_rotate(arr):
    n = len(arr)
    a = []
    for _ in arr:
        a.append(_)
    a = sorted(a)
    r_and_s = False
    for i in range(n):
        num = arr[-1]
        for j in range(n):
            if arr[j:] + arr[:j] == a:
                return True
        return False
arr = [3, 4, 1, 2]
result = left_rotate(arr)
if result == False:
    print("It is not sorted then rotated.")
else:
    print("It is rotated then sorted.")