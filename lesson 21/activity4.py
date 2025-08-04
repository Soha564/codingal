fruits = ['apple', 'banana', 'cherry']
print("Original list: ", fruits)

# Add any elements
fruits.append('orange')
print("After appending: ", fruits)

# Inserting
fruits.insert(1, 'watermelon')
print("After inserting: ", fruits)

# Changing
fruits[2] = 'plum'
print(fruits)

# Removing
fruits.remove('orange')
print("After removing: ", fruits)

# Popping
fruits.pop(1)
print("After popping:", fruits)
