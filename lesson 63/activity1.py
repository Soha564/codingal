from math import sqrt
num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, int(sqrt(num))+1): #Can do suqare root or half it - just reduce number of comparisons made.
        if (num%1) == 0:
            print(num, "is a Prime Number.")
            break
    else:
        print(num, "is not a Prime Number.")
else:
    print(num, "is not a prime number.")    