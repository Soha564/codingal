def myfunction(n):
    # First loop: O(n)
    for i in range(0, n+1):
        print("First Loop")

    # Second loop: O(log n)
    j = 1
    while j <= n+1:
        print("Second Loop", j)
        j = j * 2

    # Third loop: O(1)
    for i in range(0, 100):
        print("Third Loop")

    # Print the time complexities
print("Time complexity of First Loop: O(n+1)")
print("Time complexity of Second Loop: O(log n)")
print("Time complexity of Third Loop: O(1)")
print("Total Time Complexity: O(n)")
