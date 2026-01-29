num = int(input("Enter your original number: "))

original = num
reversed_num = 0

bits = num.bit_length()

for _ in range(bits):
    last_bit = num & 1

    reversed_num = (reversed_num << 1) | last_bit

    num >>= 1

print("Reversed Number:", reversed_num)
