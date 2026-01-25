def pos_in_binary(n):
    count = 1
    while(n):
        if(n&1 ==1):
            break
        count += 1
        n >>= 1
    return count


n = int(input("Enter a number: "))
print(pos_in_binary(n))