a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))
c = int(input("Enter the value of c:"))

print(f"Before swapping, the value of a is {a}")
print(f"Before swapping, the value of b is {b}")
print(f"Before swapping, the value of c is {c}")

temp = a
a = b
b = c
c = temp

print(f"After swapping, the value of a is {a}")
print(f"After swapping, the value of b is {b}")
print(f"After swapping, the value of c is {c}")