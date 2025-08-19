#1. Take a number from the user, create a list with all the odd numbers under the input value and another list of odd numbers.
num = int(input("Enter a number: "))

odd_numbers = [i for i in range(num) if i % 2 != 0]

print("Odd numbers from the range given: ", odd_numbers)

odd_sequence = [i for i in range(1, num * 2, 2)]


print("First", num, "odd numbers:", odd_sequence)


# 2. Create a list of fruits. Then, convert the first letter of every element to capital and create a new list of updated values.

fruits = ['apple', 'banana', 'cherry', 'watermelon', 'orange']

capitalized_fruits = [fruit.capitalize() for fruit in fruits]

print("Original list:", fruits)
print("Capitalized list:", capitalized_fruits)