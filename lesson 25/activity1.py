# Write a program to return the addition of numbers of two different lists. Then, display a list that is square of numbers of another list. Use the map() function here to get the desired result.
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

result = map(lambda a, b: a + b, numbers1, numbers2)
print("Addition of two lists: ")
print(list(result))


nums = [1, 2, 3, 4, 5]
def sq(n):
    return n ** 2

result_sq = map(sq, nums)
print("Square of numbers: ")
print(list(result_sq))
