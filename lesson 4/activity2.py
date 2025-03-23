#Write a program to calculate the number of notes in the given amount?

amount = int(input("What is your amount?"))

n500 = amount // 500
amount %= 500

n100 = amount // 100
amount %= 100

n50 = amount // 50
amount %= 50

n20 = amount // 20
amount %= 20

n10 = amount // 10
amount  %= 10

n1 = amount // 1

print("Your amount in notes is:")
print(n500, " 500 notes,")
print(n100, " 100 notes,")
print(n50, " 50 notes,")
print(n20, "20 notes,")
print (n10, "10 notes,")
print(n1, "1 notes.")