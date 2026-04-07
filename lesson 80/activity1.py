def trap(height):
    n = len(height)
    water = 0
    for i in range(n):
        left_max = max(height[:i+1])
        right_max = max(height[i:])

        water += min(left_max, right_max) - height[i]

    return water

arr = [3, 0, 2, 0, 4]
print("Water trapped: ", trap(arr))