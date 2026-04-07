def calculateProfits(prices, arr_size):
    profit = 0
    for i in range(1, arr_size):
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]
    return profit
prices = [635, 864, 247, 325, 257, 745, 245] 
profit = calculateProfits(prices, len(prices))   
print("Max profit: ", profit)