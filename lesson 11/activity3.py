num = int(input("Enter the number: ") )
str_num = str(num)
len_num = len(str_num)
original_num = num
sum = 0

while num > 0:
    # find each digit
    # number: 153, 15, 1
    digit = num % 10 # 3, 5, 1
    digit_cube = digit ** len_num # 27
    sum = sum + digit_cube # 27, 152, 153
    num = num // 10 # 153 // 10 = 15, 15 // 10 = 1, 1 // 10 = 0

if original_num == sum:
    print(original_num, "is an armstrong number.")
else:
    print(original_num, "is not an armstrong number.")