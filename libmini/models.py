class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return f"Person(Owner = '{self.name}',  email = {self.email})"


class Member(Person):
    def __init__(self, name, email):
        super().__init__(name, email)
        self._borrowed_isbn = set()
        # Using a set betcause it doesnt allow duplicates i.e one student cannnot borrow a book twice at the same time

    def borrow_book(self, isbn):
        self._borrowed_isbn.add(isbn)

    def return_book(self, isbn):
        self._borrowed_isbn.discard(isbn)


class Book:
    def __init__(self, title, author, isbn, available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', isbn='{self.isbn}', available={self.available})"


class Library:
    def __init__(self):
        self._catalog = {}
        self._loans = {}

    def add_book(self, book):
        self._catalog[book.isbn] = book

    def register_member(self, member):
        self._loans[member.email] = set()

    def borrow(self, member, isbn):
        if isbn in self._catalog and self._catalog[isbn].available:
            self._catalog[isbn].available = False
            self._loans[member.email].add(isbn)

    def return_book(self, member, isbn):
        if isbn in self._catalog and not self._catalog[isbn].available:
            self._catalog[isbn].available = True
            self._loans[member.email].discard(isbn)

    def member_loans(self, member):
        return [self._catalog[isbn] for isbn in self._loans[member.email]]

    def available_books(self):
        return [book for book in self._catalog.values() if book.available]


class Librarian(Person):
    def __init__(self, name, email):
        super().__init__(name, email)

    def register_member(self, member, library):
        library.register_member(member)

    def add_book(self, book, library):
        library.add_book(book)
