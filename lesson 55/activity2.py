class Library:
    def __init__(self):
        self.books = ["Science", "Python", "Maths", "Literature"]
    def add_book(self, book):
        self.book.append(book)
        print(book, "added successfully")

    def showcase_books(self):
        if len(self.books) == 0:
            print("No books available.")
        else:
            print("Available books: ")
            for book in self.books:
                print(" - ", book)
    def borrow_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(book, "issued successfully.")

    def return_book(self, book):
        self.books.append(book)
        print(book, "returned successfully.")
lib = Library()

while True:
    print("\n-----------Library------------")
    print("Options:")
    print("\n1. Add a book.")
    print("2. Show books.")
    print("3. Issue book.")
    print("4. Return book.")
    print("5. Exit Library")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        book = input("Enter book name: ")
        lib.add_book(book)
    elif choice == 2:
        lib.showcase_books()
    elif choice == 3:
        book = input("Enter a book name to issue: ")
        lib.borrow_book(book)
    elif choice == 4:
        book = input("Enter book name to return: ")
        lib.return_book(book)
    elif choice == 5:
        print("Thank you! Exiting Library...")
        break
    else:
        print("Invalid choice")
