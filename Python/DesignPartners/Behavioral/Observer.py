# Observer pattern: This pattern is used to define a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.
# Problem: How to define a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically?
# Solution: The Observer Pattern defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.

from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass


class Subject(ABC):

    def __init__(self):
        self.observers = []

    def register(self, observer):
        self.observers.append(observer)

    def unregister(self, observer):
        self.observers.remove(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)


class MessageBoard(Subject):

    def post_message(self, message):
        self.notify(message)

class User(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f'{self.name} received message: {message}')


# Usage
message_board = MessageBoard()
user1 = User('Alice')
user2 = User('Bob')
message_board.register(user1)
message_board.register(user2)
message_board.post_message('Hello') # Alice received message: Hello Bob received message: Hello
message_board.unregister(user2)
message_board.post_message('Hi') # Alice received message: Hi

# Output
# Alice received message: Hello
# Bob received message: Hello
# Alice received message: Hi
# Explanation
# The Observer Pattern defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically. In this example, the User class is an observer that receives messages from the MessageBoard class. The MessageBoard class is the subject that notifies the observers when a new message is posted. The User class registers with the MessageBoard class to receive notifications. When a new message is posted, the MessageBoard class notifies all registered observers, and the User class updates its state accordingly.