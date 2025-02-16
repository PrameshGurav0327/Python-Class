class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = {"title": title, "author": author, "available": True}
        self.books.append(book)
        print(f"Book '{title}' added successfully!")

    def issue_book(self, title):
        for book in self.books:
            if book["title"].lower() == title.lower() and book["available"]:
                book["available"] = False
                print(f"Book '{title}' issued successfully!")
                return
        print("Book not available or not found.")

    def return_book(self, title):
        for book in self.books:
            if book["title"].lower() == title.lower() and not book["available"]:
                book["available"] = True
                print(f"Book '{title}' returned successfully!")
                return
        print("Invalid return request.")

    def view_books(self):
        if not self.books:
            print("No books in the library.")
            return
        for book in self.books:
            status = "Available" if book["available"] else "Issued"
            print(f"Title: {book['title']}, Author: {book['author']}, Status: {status}")


def main():
    library = Library()
    
    while True:
        print("\n1. Add Book  2. Issue Book  3. Return Book  4. View Books  5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            library.add_book(title, author)
        elif choice == "2":
            title = input("Enter book title to issue: ")
            library.issue_book(title)
        elif choice == "3":
            title = input("Enter book title to return: ")
            library.return_book(title)
        elif choice == "4":
            library.view_books()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()








