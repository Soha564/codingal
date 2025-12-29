# Linear Search

lst = [1, 2, 3, 5, 6, 7]
num = int(input("Enter a number to find: "))
var = 1
for i in lst:
    if i == num:
        var = 0
        print("Element found: ", i)
        break
if var == 1:
    print("Element not found.")