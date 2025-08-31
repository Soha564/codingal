# Write a Python program to create a class that will find the numbers in the tuple that add up to a sum and return the position of elements. The value of the sum can be taken as input from the user. Tuple - (10,20,30,40,50,60,70)
class PairElements:
    def findNumbers(self, t, sum):
        lookup = {}
        for i, num in enumerate(t):
            if (sum - num) in lookup:
                return(lookup[sum - num], i)
            lookup[num] = i

sum = int(input("Enter the sum you want to search: "))

t = (10, 20, 30, 40, 50, 60, 70)

p = PairElements()
try:

    num, i = p.findNumbers(t, sum)
    print(num, i)
except:
    print("Something when wrong. Try again!")
