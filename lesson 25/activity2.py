# Write a program to return - 
# 1. zipped list from two lists 
# 2. elements of two lists zipped together, but 2nd list in reverse order 
# 3. elements of two lists zipped into a dictionary

s1 = {2, 3, 4}
s2 = {'b', 'c', 'a'}
s3 = zip(s1, s2)
print(list(s3))

list1 = [10, 20, 30]
list2 = (100, 200, 300, 400)

rev_list2 = list2[::-1]
for x, y in zip(list1, rev_list2):
    print(x, y)

stocks = ['reliance', 'infosys', 'tcs']
prices = [2175, 1128, 2750]

new_dict = {stocks: prices for stocks, prices in zip(stocks, prices)}

print(new_dict)