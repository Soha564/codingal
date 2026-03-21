def climb_stairs(n):
    if n == 0 or n ==1:
        return 1
    else:
        return climb_stairs(n-1) + climb_stairs(n-2)
n = int(input("Enter number of stairs: "))
print("Number of ways: ", climb_stairs(n))