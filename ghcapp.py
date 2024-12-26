# Create empty book library list
book_library = []  # library book
borrowed_book = []  # books on loan


# Function to add a book to the library

def add_book():
    book_title = input("Please enter book title: ")
    author = input("Please enter book author: ")

    while True:
        try:
            year_of_publication = int(
                input("Please enter the book's year of publication (as a positive whole number): "))
            if year_of_publication <= 0:
                print("Year of publication must be a positive whole number. Please try again.")
            else:
                break  # Exit loop if the input is valid
        except ValueError:
            print("Year of publication must be a valid integer. Please try again.")

    # Create a dictionary of book info
    book_library.append({"Title": book_title, "Author": author, "Year of Publication": year_of_publication})
    print(f"Book '{book_title}' added successfully.")

# Function to exit the application

def exit_app():
    print("Exiting the application. Goodbye!")
    exit()

# Function to view books in the library

def view_books():
    if not book_library:
        print("No books available in the library.")
    else:
        print("\nBooks in Library:")
        for book in book_library:
            print(f"Title: {book['Title']}, Author: {book['Author']}, Year: {book['Year of Publication']}")

# Function to search for a book in the library

def search_book(book_library, book_title):
    for book in book_library:
        if book["Title"].lower() == book_title.lower():  # Case-insensitive search
            return f"The book '{book_title}' by {book['Author']} was found in the library."
    return f"The book '{book_title}' was not found in the library."

# Function to view books currently on loan

def view_books_on_loan():
    if not borrowed_book:
        print("No books are currently on loan.")
    else:
        print("\nBooks on Loan:")
        for book in borrowed_book:
            print(f"Title: {book['Title']}, Author: {book['Author']}, Year: {book['Year of Publication']}")

# Function to borrow a book from the library

def borrow_book(book_library):
    book_to_borrow = input("Please enter the book title to borrow: ")
    for book in book_library:
        if book["Title"].lower() == book_to_borrow.lower():  # Case-insensitive match
            book_library.remove(book)
            borrowed_book.append(
                {"Title": book["Title"], "Author": book["Author"], "Year of Publication": book["Year of Publication"]})
            return f"The book '{book_to_borrow}' by {book['Author']} was borrowed."
    return f"The book '{book_to_borrow}' is not available in the library."

# Function to return a borrowed book to the library

def return_book(borrowed_book):
    book_to_return = input("Please enter the book title to return: ")
    for book in borrowed_book:
        if book["Title"].lower() == book_to_return.lower():  # Case-insensitive match
            borrowed_book.remove(book)
            book_library.append(
                {"Title": book["Title"], "Author": book["Author"], "Year of Publication": book["Year of Publication"]})
            return f"The book '{book_to_return}' by {book['Author']} was successfully returned to the library."
    return f"The book '{book_to_return}' was not found in the borrowed books."

# Function to display the menu and handle user choices

def menu():
    while True:
        print("\n=== Library Management System ===")
        print("1. Add a New Book")
        print("2. View Books")
        print("3. Borrow a Book")
        print("4. Search for a Book")
        print("5. View Books on Loan")
        print("6. Return a Book")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            add_book()  # function call
        elif choice == "2":
            view_books()
        elif choice == "3":
            print(borrow_book(book_library))
        elif choice == "4":
            book_title = input("Please enter book title: ")
            print(search_book(book_library, book_title))
        elif choice == "5":
            view_books_on_loan()
        elif choice == "6":
            print(return_book(borrowed_book))
        elif choice == "7":
            exit_app()
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


# Run the program
if __name__ == "__main__":
    menu()

