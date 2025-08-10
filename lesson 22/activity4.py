# Find the sum and average of a tuple.

def findsum(t):
    sum = 0
    for i in t:
        sum += i
    return sum
def findavg(t):
    sum = findsum(t)
    total = len(t)
    return sum / total

t = (3, 4, 7, 2, 9, 2, 5)
print("Sum of the tuple:", findsum(t))
print("Average of the tuple:", findavg(t))
