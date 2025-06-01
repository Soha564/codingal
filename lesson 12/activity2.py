# Write a program to check how many times a character is repeated in a word.

text = input("Enter the text: ")
char = input("Enter the character: ")
#text: hello, char: 1, count: 2

count = 0

for x in text: # text:hello 
    #1st iteration: x = h
    #2nd iteration: x = e
    #3rd iteration: x = l
    #4th iteration: x = l
    #5th iteration: x = o
    #print(x)
    if x.lower() == char.lower(): # char: l 
        count += 1
print(char, "appears", count, "times.")
