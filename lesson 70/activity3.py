def add(n):
    if(n==1 or n==0):
        return 1
    return n+add(n-1)
n = int(input("Enter a number: "))
print("Factorial of", n, "is: ", add(n))    
