def reverseNumber(n, rev):
    if n == 0:
        return rev
    l_d = n%10
    rev = (rev*10) + l_d
    return reverseNumber((n//10), rev)
n = int(input("Enter a number: "))
rev = 0
print("Reversed number is: ", reverseNumber(n, rev))

