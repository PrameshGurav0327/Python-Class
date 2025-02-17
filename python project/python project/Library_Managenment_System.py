import datetime

library = []

class Books:
    def __init__(self):
        self.books = []
        self.issued_books = []

    def add_book(self):
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        book = {
            "Book ID": book_id,
            "Title": title,
            "Author": author
        }

        self.books.append(book)
        print("Book added successfully!")

    def issue_book(self):
        title = input("Enter title of the book to issue: ")
        author = input("Enter author of the book to issue: ")
        member = input("Enter name of the member issuing the book: ")

        try:
            member_phone_no = int(input("Enter 10-digit phone number: "))
        except ValueError:
            print("Invalid phone number. Please enter numbers only.")
            return

        issue_date = datetime.datetime.now()

        book_to_issue = {
            "Title": title,
            "Author": author,
            "Member": member,
            "Phone No": member_phone_no,
            "Issue Date": issue_date
        }

        self.issued_books.append(book_to_issue)
        print("Book issued successfully!")

    def view_books(self):
        if not self.books:
            print("No books available in the library.")
            return

        for book in self.books:
            print(f"Book ID: {book['Book ID']}, Title: {book['Title']}, Author: {book['Author']}")

    def view_issued_books(self):
        if not self.issued_books:
            print("No books have been issued.")
            return

        for book in self.issued_books:
            print(f"Title: {book['Title']}, Issued to: {book['Member']}, Phone: {book['Phone No']}, Date: {book['Issue Date']}")

library_system = Books()

while True:
    print("\n1. Add a Book")
    print("2. Issue a Book")
    print("3. View Available Books")
    print("4. View Issued Books")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        library_system.add_book()
    elif choice == "2":
        library_system.issue_book()
    elif choice == "3":
        library_system.view_books()
    elif choice == "4":
        library_system.view_issued_books()
    elif choice == "5":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")
