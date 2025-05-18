text = "Python"
for i in text:
    print(i)

print("________________________")
for x in range(1, 11, 3):
    print(x)

print("________________________")

nth = int(input("Enter the nth number to find the sum of natural numbers:"))

sum = 0

for y in range ( 1, nth + 1):
    sum += y # sum = sum + y

print(f"Sum of {nth} natural numbers: {sum}")

