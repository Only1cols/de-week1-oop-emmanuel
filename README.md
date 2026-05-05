
# libmini — Library Checkout System
A minimal python package that models a library checkout workflow, 
buit to demonstrate core OOP principles and the factory design pattern.


## OOP Concepts

**Class** 

— a blueprint for creating objects. For example, 
"book" is a class that defines what every book object looks like.

**Object/Instance** 

— a concrete item created from a class.
For example, "Book("Things fall apart","Chinua achebe", "ISBN001") is an instance of "Book".

**Encapsulation**

 — Bundling data and methods together while 
hiding internal details behind a clean interface. 
In this project, "library" stores "_catalog" and "_loans" as private attributes (leading underscore"),
exposing them only through methods like 'borrow()' and 'available_books()'.

**Inheritance** 

— deriving a new class from an existing one to reuse and extend behavior.
Both "member" and 'librarian' inherit from 'person', gainiong 'name' and 'email' automatically.


**Polymorphism** 

— same method name, different behaviors depending on the object.
'EmailNotofier' and 'SmsNotifier' both implement '.send()' but each behave differently.

---

## My Approach

I started by identifying the core entities in a real library:
people,books, and thhe library itself.

-'person' is the base class for anyone interacting with the system.

-'Member' extends 'Person' with the ability to borrow and return books,tracking borrowed ISBNs
 in a 'set' to prevent dupllicates.

-'Librarian' extends 'Person' with the ability to add books and register members into the library.

-'Book' is a standalpne class holding book details and availability status.

-'Library' is the central hub- it owns the catalog and loan records, and all checkout logic lives here.

I used **composition** for 'Library' i.e it doesnt inherit from anything, it owns books and members internally.


## Factory Pattern
The factory pattern lets you create objects without specifying the exact class upfront.
 Instead of calling "EmailNotifier()' or 'SmsNotifier()' directly, you ask the factory:

 ```python

 notifier = NotifierFactory.create("Email")
 notifier.send(member.email, "you borrowed: Things fall apart")


Project Structure
	•	libmini/models.py — Person, Member, Librarian, Book, Library
	•	libmini/notify.py — Notifier, EmailNotifier, SMSNotifier, NotifierFactory
	•	libmini/cli.py — CLI demo


## How to Run

  python3 -m venv .venv && source .venv/bin/activate
  python3 -m libmini.cli



##Sample Output##

Books added to library:
  -Things fall apart by Chinua Achebe
  -Half of a yellow sun by Chimamanda Ngozi Adichie
  -purple Hibiscus by Chimamanda Ngozi Adichie
Members registered:
 - Emmanuel
 - Ebuka
 Borrowing books: 
 Emmanuel borrowed: Things fall apart
 Ebuka borrowed: Half of a yellow sun
Emmanuel's current loaned books:
 -Things fall apart
Available books
 - purple Hibiscus
returning things fall apart......
available books after return:
  -Things fall apart by Chinua Achebe
  -purple Hibiscus by Chimamanda Ngozi Adichie
  
Email sent to emmanuelebuka@gmail.com: you borrowed: Things Fall Apart
Sms sent to ebuka123@gmail.com: you borrowed: Half of a yellow sun

    