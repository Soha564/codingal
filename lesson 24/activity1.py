# Write a program to create a set and perform the following operations on that set- 1. Create a set with integer elements 2. Create a set with mixed data type elements 3. Create another set with elements - 1, 2, 3, 4, 3, 2 4. Create a set from a list with elements - [1, 2, 3, 2] 5. Print the set after removing the first element from this set - [0, 1, 3, 4, 5]

setA = {5, 6, 8, 5}
print(setA)

setB = {6, 7.4, "set", True}
print(setB)

setC = {1, 2, 3, 4, 3, 2}
print("Set C:", setC)
listC = list(setC)
print("List C:", listC)

# setD = set([0, 2, 4])
# print(setD)

setE = set([0, 1, 3, 4, 5])
print("Before Popping:", setE)
setE.pop() # automatically removes first element without typing which element
print("After Popping:", setE)