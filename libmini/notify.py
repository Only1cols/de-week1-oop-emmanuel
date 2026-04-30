from abc import ABC, abstractmethod


class Notifier(ABC):
    @abstractmethod
    def send(self, receiver, message):
        pass


class EmailNotifier(Notifier):

    def send(self, receiver, message):
        return f"Email sent to {receiver}: {message}"


class SMSNotifier(Notifier):
    def send(self, receiver, message):
        return f"Sms sent to{receiver}: {message}"


class NotifierFactory:
    @staticmethod
    def create(kind):
        if kind == "email":
            return EmailNotifier()
        elif kind == "sms":
            return SMSNotifier()
