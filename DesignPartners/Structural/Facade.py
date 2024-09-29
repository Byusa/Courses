# Facade pattern: This pattern provides a unified interface to a set of interfaces in a subsystem. Facade defines a higher-level interface that makes the subsystem easier to use.
# Problem: How to provide a unified interface to a set of interfaces in a subsystem?
# Solution: The Facade Pattern provides a unified interface to a set of interfaces in a subsystem.

from abc import ABC, abstractmethod


class Dog(ABC):
    @abstractmethod
    def bark(self):
        pass


class Cat(ABC):
    @abstractmethod
    def meow(self):
        pass


class DogAdapter(Cat):
    def __init__(self, dog):
        self.dog = dog

    def meow(self):
        return self.dog.bark()


class Poodle(Dog):
    def bark(self):
        return 'Poodle says Woof'


class Rottweiler(Dog):
    def bark(self):
        return 'Rottweiler says Wuff'


# Usage
poodle = Poodle()
rottweiler = Rottweiler()
dog_adapter = DogAdapter(poodle)
print(dog_adapter.meow()) # Poodle says Woof
