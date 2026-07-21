text = input("Enter a string: ")

cleaned = ""
extra = [" ", "\n", "\t"]
for char in text:
    if char not in extra:
        cleaned += char

print(cleaned)