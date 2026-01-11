# Method 1

num = int(input("Enter a number: "))
if str(num) == str(num)[::-1]:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")

# Method 2

num = int(input("Enter a number: "))
orig = num
reverse = 0
while num > 0:
    n = num%10
    reverse = reverse*10 + n
    num //= 10
if orig == reverse:
    print("It is a palindrome.")
else:
    print("it is not a palindrome")