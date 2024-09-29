# Decorator Pattern: This pattern is used to add new functionality to an existing object without altering its structure.\
# Problem: How to add new functionality to an existing object without altering its structure?
# Solution: The Decorator Pattern adds new functionality to an existing object without altering its structure.

# use a dog and cat example for decorator pattern
from abc import ABC, abstractmethod 


class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return 'Dog says Woof'


class Cat(Animal):
    def speak(self):
        return 'Cat says Meow'


class AnimalDecorator(Animal):
    def __init__(self, animal):
        self.animal = animal

    def speak(self):
        return self.animal.speak()


class LoudBarkDecorator(AnimalDecorator):
    def speak(self):
        return f'{self.animal.speak()} Woof Woof'


class LoudMeowDecorator(AnimalDecorator):
    def speak(self):
        return f'{self.animal.speak()} Meow Meow'


# Usage
dog = Dog()
loud_dog = LoudBarkDecorator(dog)
print(loud_dog.speak()) # Dog says Woof Woof
