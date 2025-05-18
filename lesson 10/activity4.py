text = input("Enter a sentence of your choice:")
word_counter = 0

#split() converts string to a list.
text_list = text.split()
print(text_list)
for word in text_list:
    print(word)
    word_counter += 1

print ("N.o of words:", word_counter)