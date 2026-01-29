def reverse_bits(n):
    result = 0
    while n > 0:
        result = (result << 1) | (n & 1)
        n >>= 1
    return result

original = int(input("Enter your original number: "))
reversed_number = reverse_bits(original)
print(f"Reversed Number: {reversed_number}")
