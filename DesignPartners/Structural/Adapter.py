# Adapter pattern: This pattern allows incompatible interfaces to work together. It wraps an existing class with a new interface so that it becomes compatible with the client code.
# Problem: How to make incompatible interfaces work together?
# Solution: The Adapter Pattern wraps an existing class with a new interface so that it becomes compatible with the client code.

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