# Write to check if a person is buying oranges at 100 rs and later selling it 1at 120 rs. Find that he has profit or loss?

buying_price = 100
selling_price = 120

if selling_price > buying_price:
    print("The profit is:", selling_price - buying_price, "rs." )
else:
    print("The loss is:", buying_price - selling_price, "rs.")