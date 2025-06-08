# Floyd's triangle
rows = int(input("Enter the number of rows: "))
count = 0
for i in range(1, rows+1):
    for j in range(1, i+1):
        count += 1
        print(count, end=(" "))
    print()