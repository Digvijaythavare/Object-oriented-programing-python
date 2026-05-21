class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
class Library():
    def __init__(sel):
        self.books = []        
    def add_book(self,book):
        self.books.append(book)
    def display_books(self):
        for book in self.books:
            print(f"{book.title} by {book.author}") 

book1 = Library()
book1.add_book(book=("vijay","kamvasna"))
book1.display_books()