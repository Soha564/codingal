# Write a program to check the frequency of a value in a dictionary - {'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}.

dict = {'Codingal' : 2, 'is' : 2, 'best' : 3, 'for' : 2, 'coding' : 1}

k = 2

counter = 0

for key in dict:
    if dict[key] == k:
        counter = counter + 1

print(k, "appears", counter, "times.")