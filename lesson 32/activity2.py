class Flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning

    def __str__(self):
        # We are retruning a string
        return self.word+ ' ( '+self.meaning+' )'

flashcards = []
print("Welcome to the flashcard application.")

while True:
    word = input("Enter the name you want to add to the flashcard: ")
    meaning = input("Enter the meaning of the word: ")

    flashcards.append(Flashcard(word, meaning))
    option = int(input("Enter 0, if you want to add another flashcard, otherwise enter 1: "))

    if option:
        break

# Printing all flashcards

print("\nYour flashcards: ")
for i in flashcards:
    print(">", i)