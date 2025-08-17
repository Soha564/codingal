# Write a program to find the intersection, union, difference and symmetric difference of two sets. Set1 = {green, blue} Set2 = {blue, yellow}.

Set1 = {'green', 'blue'} 
Set2 = {'blue', 'yellow'}
print("Set 1:", Set1)
print("Set 2:", Set2)

print("\nIntersection :", Set1.intersection(Set2))

print("\nUnion :", Set1.union(Set2))

print("\nDifference :", Set1.difference(Set2))
print("\nDifference :", Set2.difference(Set1))

print("\nSymmetric Difference :", Set1.symmetric_difference(Set2))

print("\n")




