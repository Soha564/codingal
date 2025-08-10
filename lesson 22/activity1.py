t = ("Python", 3.13, True)
print(t)

t1 = (4, 5, 7, 2)
print(t1)
print("First element:", t1[0])
print("Last element:", t1[-1])

t2 = t1 + (9,)
print(t2)

print("No. of elements:", len(t2))

t3 = (30, 50, 20, 50, 10, 50)

print("50 has occurred:", t3.count(50), "times.")

t4 = (1, 2, 3, 4, 5, 6, 7, 8)
print("Slicing:", t4[2:6])

# cannot modify list (add, take away etc.)