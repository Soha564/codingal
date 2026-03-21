coins = [500, 100, 10, 5, 1]

def solve(n, index, current):
    if index == len(coins) - 1:
        current[index] = n   
        print(current)
        return

    coin = coins[index]
    max_use = n // coin
    for count in range(max_use + 1):
        current[index] = count
        solve(n - count * coin, index + 1, current)
        

n = int(input("Enter n = "))
solve(n, 0, [0]*5)
