def multiply_one_step(a, b):
    return a * b

def multiply_n_steps(a, b):
    total = 0
    for i in range(b):
        total += a
    return total

a = int(input("Enter a: "))
b = int(input("Enter b: "))

print("1 iteration:", multiply_one_step(a, b))
print("N iterations:", multiply_n_steps(a, b))
