def is_power_of_two(n):
    if n == 1:
        return True
    if n <= 0 or n % 2 != 0:
        return False
    
    return is_power_of_two(n // 2)

num = int(input("Enter a number: "))

if is_power_of_two(num):
    print(num, "is a power of 2")
else:
    print(num, "is NOT a power of 2")
