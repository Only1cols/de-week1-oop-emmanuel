
# libmini — Library Checkout System

## OOP Concepts

**Class** — a blueprint for creating objects.

**Object/Instance** — a concrete item created from a class.

**Encapsulation** — bundling data and methods; hiding internal details behind a clean interface.

**Inheritance** — deriving a new class from an existing one to reuse and extend behavior.

**Polymorphism** — same method name, different behaviors depending on the object.

## Factory Pattern
A creational pattern where a factory method creates objects without exposing the creation logic. Used here in `NotifierFactory` to return either an `EmailNotifier` or `SMSNotifier` based on a string input.

## How to Run

```bash
python -m venv .venv && source .venv/bin/activate
python -m libmini.cli



Project Structure
	•	libmini/models.py — Person, Member, Librarian, Book, Library
	•	libmini/notify.py — Notifier, EmailNotifier, SMSNotifier, NotifierFactory
	•	libmini/cli.py — CLI demo
    