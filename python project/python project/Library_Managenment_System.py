import datetime

class Library:
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
            "Author": author,
            "Issued": False
        }

        self.books.append(book)
        print("Book added successfully!")

    def issue_book(self):
        title = input("Enter title of the book to issue: ")
        author = input("Enter author of the book to issue: ")

        for book in self.books:
            if book["Title"].lower() == title.lower() and book["Author"].lower() == author.lower():
                if book["Issued"]:
                    print("Book is already issued.")
                    return

                member = input("Enter name of the member issuing the book: ")
                phone_no = input("Enter 10-digit phone number: ")

                if not phone_no.isdigit() or len(phone_no) != 10:
                    print("Invalid phone number. Please enter exactly 10 digits.")
                    return

                return_date = input("Enter return date (YYYY-MM-DD): ")

                book["Issued"] = True 
                issued_book = {
                    "Title": title,
                    "Author": author,
                    "Member": member,
                    "Phone No": phone_no,
                    "Issue Date": datetime.datetime.now().strftime("%Y-%m-%d"),
                    "Return Date": return_date
                }
                self.issued_books.append(issued_book)
                print("Book issued successfully!")
                return

        print("Book not found in the library.")

    def return_book(self):
        title = input("Enter title of the book to return: ")

        for book in self.books:
            if book["Title"].lower() == title.lower() and book["Issued"]:
                book["Issued"] = False
                
                for issued in self.issued_books:
                    if issued["Title"].lower() == title.lower():
                        print(f"Book '{title}' returned by {issued['Member']}.")
                        self.issued_books.remove(issued)
                        return
        print("Book not found or not issued.")

    def view_books(self):
        if not self.books:
            print("No books available in the library.")
            return

        for book in self.books:
            status = "Issued" if book["Issued"] else "Available"
            print(f"Book ID: {book['Book ID']}, Title: {book['Title']}, Author: {book['Author']}, Status: {status}")

    def view_issued_books(self):
        if not self.issued_books:
            print("No books have been issued.")
            return

        for book in self.issued_books:
            print(f"Title: {book['Title']}, Issued to: {book['Member']}, Phone: {book['Phone No']}, Issue Date: {book['Issue Date']}, Return Date: {book['Return Date']}")


library_system = Library()

while True:
    print("\n1. Add a Book")
    print("2. Issue a Book")
    print("3. Return a Book")
    print("4. View Available Books")
    print("5. View Issued Books")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        library_system.add_book()
    elif choice == "2":
        library_system.issue_book()
    elif choice == "3":
        library_system.return_book()
    elif choice == "4":
        library_system.view_books()
    elif choice == "5":
        library_system.view_issued_books()
    elif choice == "6":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")




