a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))

print(f"Before swapping, the value of a is {a}")
print(f"Before swapping, the value of b is {b}")

temp = a
a = b
b = temp

print(f"After swapping, the value of a is {a}")
print(f"After swapping, the value of b is {b}")