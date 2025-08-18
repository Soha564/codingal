# List Comprehension
a = [5, 7, 2, 9, 8, 4]
# Find all the odd numbers in the list
b = [i for i in a if i % 2 != 0]
print(b)

# Dictionary Comprehension
# Find the squares
c = {x : x ** 2 for x in a}
print(c)