# Write a program to check whether the given tuple - (1,2,3,3,2,1) is a palindrome or not. If it's a palindrome, then it is the same after being reversed.
# Example: madam = madam

def is_palindrome(t):
    first_index = 0 
    last_index = len(t) - 1
    
    while first_index < last_index:
        if t[first_index] != t[last_index]:
            return False
        first_index += 1
        last_index -= 1
    return True

t = (1, 2, 3, 3, 2, 1)
if is_palindrome(t):
    print("It's a palindrome")
else:
    print("It's not a palindrome")