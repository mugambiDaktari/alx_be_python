class Book:
    def __init__(self, title, author, is_checked_out=False):
        self.title = title
        self.author = author
        self.__is_checked_out = is_checked_out  # Private attribute

    def is_checked_out(self):
        return self.__is_checked_out

    def check_out(self):
        if not self.__is_checked_out:
            self.__is_checked_out = True
            return True
        return False

    def return_book(self):
        if self.__is_checked_out:
            self.__is_checked_out = False
            return True
        return False





class Library:
    def __init__(self):
        self.__books = [] 

    def add_book(self, book):
        if isinstance(book, Book):
            self.__books.append(book)  

    def check_out_book(self, title):
        for book in self.__books:
            if book.title == title and not book.is_checked_out():
                if book.check_out():
                    return f"Book '{title}' has been checked out."
        return f"Book '{title}' is not available."
    
    def return_book(self, title):
        for book in self.__books:
            if book.title == title and book.is_checked_out():
                if book.return_book():
                    return f"Book '{title}' has been returned."
        return f"Book '{title}' was not checked out."

    def list_available_books(self):
     return [f"{book.title} by {book.author}" for book in self.__books if not book.is_checked_out()]
    
""" library = Library()
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")

library.add_book(book1)
library.add_book(book2)

print(library.list_available_books())

print(library.check_out_book("1984"))
print(library.check_out_book("1984"))
print(library.list_available_books())
print(library.return_book("1984"))
print(library.list_available_books()) """

library = Library()
library.add_book(Book("Brave New World", "Aldous Huxley"))
library.add_book(Book("1984", "George Orwell"))

    # Initial list of available books
print("Available books after setup:")
print(library.list_available_books())

    # Simulate checking out a book
print(library.check_out_book("1984"))
print("\nAvailable books after checking out '1984':")
print(library.list_available_books())

    # Simulate returning a book
print(library.return_book("1984"))
print("\nAvailable books after returning '1984':")
print(library.list_available_books())