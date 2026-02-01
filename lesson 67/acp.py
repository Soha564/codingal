def power8(number):
    if number <= 0:
        return 0

    # Check if number is a power of 2
    if (number & (number - 1)) != 0:
        return 0

    # Count how many times we can divide by 2
    count = 0
    while number > 1:
        number //= 2
        count += 1

    # Power of 8 means exponent is divisible by 3
    return 1 if count % 3 == 0 else 0


number = int(input("Enter a number: "))
if power8(number):
    print("The number is a power of 8.")
else:
    print("The number is not a power of 8.")
