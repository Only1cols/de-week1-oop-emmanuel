from libmini.models import Library, Member, Librarian, Book
from libmini.notify import NotifierFactory


def main():
    library = Library()
    librarian = Librarian("Mr Tunde", "tunde@gmail.com")

    # Add Books
    book1 = Book("Things fall apart", "Chinua Achebe", "ISBN001")
    book2 = Book("Half of a yellow sun", "Chimamanda Ngozi Adichie", "ISBN002")
    book3 = Book("purple Hibiscus", "Chimamanda Ngozi Adichie", "ISBN003")

    librarian.add_book(book1, library)
    librarian.add_book(book2, library)
    librarian.add_book(book3, library)

    # Register members
    member1 = Member("Emmanuel", "emmanuelebuka@gmail.com")
    member2 = Member("Ebuka", "ebuka123@gmail.com")

    librarian.register_member(member1, library)
    librarian.register_member(member2, library)

    # Borrow Books
    library.borrow(member1, "ISBN001")
    library.borrow(member2, "iSBN002")

    # send notifications
    notifier = NotifierFactory.create("email")
    print(notifier.send(member1.email, "you borrowed: Things Fall Apart"))

    notifier2 = NotifierFactory.create("sms")
    print(notifier2.send(member2.email, "you borrowed:Half of a yellow sun"))

    # print loans and available books
    print("Emmanuel's loans:", library.member_loans(member1))
    print("Available books:", library.available_books())

    # return a book
    library.return_book(member1, "ISBN001")
    print("After return, available books:", library.available_books())


if __name__ == "__main__":
    main()
