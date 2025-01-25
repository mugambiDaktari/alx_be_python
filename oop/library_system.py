class Book:
    def __init__(self, title, author):
        if not isinstance(title, str) and not isinstance(author, str):
            raise TypeError("Both title and author must be strings")
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"    

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        if not isinstance(file_size, int):
            raise TypeError("File size must be an integer")
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File size: {self.file_size}KB"

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        if not isinstance(page_count, int):
            raise TypeError("Page count must be an integer")
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page count: {self.page_count}"

class Library:
    books = []
    

    @classmethod
    def add_book(cls, book):
        if isinstance(book, Book) or isinstance(book, EBook) or isinstance(book, PrintBook):
            cls.books.append(book)

    @classmethod
    def list_books(cls):
        for book in cls.books:
            print(str(book)) 



