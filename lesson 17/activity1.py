# Write a program to check alphabet “A” is present in the given string or not. And terminate the loop after finding the alphabet “A.”
word = input("Enter a word: ")
#program to check break keyword
for i in word: #iterate fo loop
    if (i == "A" or i == "a"): # condition 1
    #display result
        print("A is found")
        break #breaking statement
    else:
    #display result
        print("A is not found")