dict = {'Codingal' : 3, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}
print(dict)
k = int(input("Enter a number from above:"))

counter = 0

for key in dict:
    if dict[key] == k:
        counter = counter + 1

print("The frequency for", k, "is", counter)
