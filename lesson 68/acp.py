num = int(input("Enter your number: "))

current = 0
longest = 0
n = num

while n > 0:
    if n & 1:          
        current += 1
        longest = max(longest, current)
    else:
        current = 0
    n >>= 1            

print("Longest consecutive 1’s length :", longest)
