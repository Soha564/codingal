def max_product_pair(arr):
    max1 = max(arr)
    arr.remove(max1)
    max2 = max(arr)
    
    return max1, max2, max1 * max2


size = int(input("Enter size of array: "))

print("Start entering elements (only positive integers) of array, each element in a new line:\n")
arr = []
for i in range(size):
    arr.append(int(input()))

a, b, product = max_product_pair(arr)

print(f"\nElements that make up the maximum product: [{b}, {a}]")
print(f"Maximum Product is equal to: {product}")
