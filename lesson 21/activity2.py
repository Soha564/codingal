# Write a Python program to count the number of strings where the string length is two or more, and the first and last characters are the same from a given list of strings.
text = "aba"

if text[0] == text[-1]:
    print("Same charcater.")

words = ["abc", "cdf", "xyx", "rsr", "qty"]
result = []

for word in words:
    if word[0] == word[-1]:
        result.append(word)
print(result)