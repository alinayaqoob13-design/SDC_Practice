# ---- DEFINE BOOK CLASS ----
class Book:
    # Constructor to initialize book details
    def __init__(self, title, author, year, available=True):
        self.title = title           # Book title
        self.author = author         # Book author
        self.year = year             # Publication year
        self.available = available   # Availability status (default True)

    # Method to borrow the book
    def borrow(self):
        if self.available:           # Check if book is available
            self.available = False   # Mark book as borrowed
            print(f"'{self.title}' has been borrowed.")  # Confirmation message
        else:
            print(f"Sorry, '{self.title}' is already borrowed.")  # Already borrowed

    # Method to return the book
    def return_book(self):
        if not self.available:       # Check if book was borrowed
            self.available = True    # Mark book as available
            print(f"'{self.title}' has been returned and is now available.")  # Confirmation
        else:
            print(f"'{self.title}' was not borrowed.")  # Book was not borrowed

# ---- CREATE BOOK OBJECTS ----
book1 = Book("Information Security", "Alina Yaqoob", 2004)  # Book 1
book2 = Book("Mobile Application Development", "Ayesha Asif", 2005)  # Book 2

# ---- BORROW AND RETURN OPERATIONS ----
book1.borrow()         # Borrow book1
book1.return_book()    # Return book1

book2.borrow()         # Borrow book2
book2.borrow()         # Try to borrow again (should show already borrowed)
book2.return_book()    # Return book2
