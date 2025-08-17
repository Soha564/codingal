# Write a program to create an array with the following elements - [1, 3, 5, 3, 7, 9, 3]. Then find the number of occurrences of number 3 in the array. Also, print the reversed array.

import array as arr

array_num = arr.array('i', [1, 3, 5, 3, 7, 9, 3])
print("Original array: ", array_num)

for i in array_num:
    print(i)

print("3 occurs:", array_num.count(3), " times.")

array_num.reverse()
print("Reversed array:", array_num)
