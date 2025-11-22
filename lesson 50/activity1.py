# Factorial number = 5 -> 5 x 4 x 3 x 2 x 1
def recursion_factor(n):
    if n == 1:
        return n
    else: 
        return n*recursion_factor(n-1)

n = int(input("Enter a number: "))
sum = recursion_factor(n)
print("The factorial of this number is: ", sum)