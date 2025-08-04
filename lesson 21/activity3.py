# Write a Python program to find the sum and average of the list. The average of the list is defined as the sum of the elements divided by the number of the elements. Also, find the largest and the smallest number in the list.

l = [2, 4, 9, 6, 7, 8]

print("The original list: ", l)

sum = 0
for i in l:
    sum = sum + i

print("Sum:", sum) 

print("Number of elements that are in the list: ", len(l))

avg = sum / len(l)
print("Avg:", avg)

l.sort()
print("Sorted list (in ascending order): ", l)

print("Min number: ", l[0])
print("Max number: ", l[-1])
