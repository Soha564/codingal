a = [] # empty list
print(type(a))
print(a)


numbers = [4,2,3,7]
#          0 1 2 3
#         -4-3-2-1
print(numbers)

print("First element:", numbers[0])
print("Second element:", numbers[1])
print("Third element:", numbers[2])
print("Last element:", numbers[-1])

triple = [1, 2, 3, 4] * 3
print(triple)

alist = [500, 22, 334, 299, 32]
alist = alist[::-1]
print("Reverse order:", alist)
