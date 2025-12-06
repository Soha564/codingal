s = {1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 5}
print(s)

s.add(6)
s.add(7)
print("Updated set: ", s)

s1 = s
s2 = {6, 6, 6, 6, 7, 7, 7, 7, 8, 9}
print("\nSet1: ", s1)
print("Set 2: ", s2)
print("Difference: ")
print(s1.difference(s2))
print("Symmetric Difference: ")
print(s1.symmetric_difference(s2))

print(s1.union(s2))
print(s1.intersection(s2))