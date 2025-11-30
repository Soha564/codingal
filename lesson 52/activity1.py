list = ["banana", "apple", "orange", "mango", "watermelon"]

print("Length of the list: ", len(list))
print("First Element: ", list[0])
print("Last Element: ", list[-1])

list.append("kiwi")
print("Updated list: ", list)

list.sort()
print("Sorted List: ", list)

list.pop()
print("Updated list: ", list)

list.reverse()
print("Reversed list: ", list)

print("Multiplication on list: ", list*2)

list = list[:4]
print("Sliced list: ", list)

list.clear()
print("CLeared list: ", list)