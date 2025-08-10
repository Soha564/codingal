# Write a Python program to calculate the product of first the ven numbers then the odd numbers from the numbers of the given tuple. 
def findmultiple(t):
    even_product = 1
    odd_product = 1
    for i in t:
        if i % 2 == 0:
            even_product *= i
        else:
            odd_product *= i

    return even_product, odd_product

t = (1, 2, 3, 4, 5, 6, 7, 8)
even_result, odd_result = findmultiple(t)

print("Product of even numbers:", even_result)
print("Product of odd numbers:", odd_result)
