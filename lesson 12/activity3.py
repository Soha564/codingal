# Write a program to print all the prime numbers which come in the range entered by the user

num = int(input("Enter a number: "))

# let's take a flag to track if the number is prime or not. initially, let's assume the number is prime.

is_prime = True

# normally, prime numbers are greater than 1
if num <= 1:
     is_prime = False
else:
     #find factors from 2 to num - 1
     #because we cannot take 1 and the number itself
     factor = 2

     while factor < num:
        # if the number is divisible by the factor, then it has a fator
        # so it is not a prime number.
        if num % factor == 0:
               is_prime = False
               break
        factor += 1 # go to next number
# let's check the result using the flag is_prime
if is_prime:
     print(num, "is prime")
else:
     print(num, "is not prime")
     