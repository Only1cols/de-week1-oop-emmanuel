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

    print(" Books added to library:")
    for book in library.available_books():
        print(f"  -{book.title} by {book.author}")

    # Register members
    member1 = Member("Emmanuel", "emmanuelebuka@gmail.com")
    member2 = Member("Ebuka", "ebuka123@gmail.com")

    librarian.register_member(member1, library)
    librarian.register_member(member2, library)

    print(" Members registered:")
    print(f" - {member1.name}")
    print(f" - {member2.name}")

    # Borrow Books
    library.borrow(member1, "ISBN001")
    library.borrow(member2, "iSBN002")

    print(" borrowing books.....")
    library.borrow(member1, "ISBN001")
    print(F" {member1.name} borrowed: Things fall apart")
    library.borrow(member2, "ISBN002")
    print(F" {member2.name} borrowed: Half of a yellow sun")

    # send notifications
    notifier = NotifierFactory.create("email")
    print(notifier.send(member1.email, "you borrowed: Things Fall Apart"))

    notifier2 = NotifierFactory.create("sms")
    print(notifier2.send(member2.email, "you borrowed:Half of a yellow sun"))

    # loans
    print(f"{member1.name}'s current loaned books:")
    for book in library.member_loans(member1):
        print(f" -{book.title}")

    # available books
    print(f"Available books")
    for book in library.available_books():
        print(f". - {book.title}")
    # return a book
    print("returning things fall apart......")
    library.return_book(member1, "ISBN001")
    print("available biooks after return:")
    for book in library.available_books():
        print(f"  -{book.title} by {book.author}")


if __name__ == "__main__":
    main()
