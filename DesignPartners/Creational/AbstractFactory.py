# Abstract Factory Pattern: This pattern provides an interface for creating families of related or dependent objects without specifying their concrete classes.
# Problem: How to create families of related or dependent objects without specifying their concrete classes?
# Solution: The Abstract Factory Pattern provides an interface for creating families of related or dependent objects without specifying their concrete classes.

from abc import ABC, abstractmethod

class Dog(ABC):
    @abstractmethod
    def speak(self):
        pass

class Cat(ABC):
    @abstractmethod
    def speak(self):
        pass

class DogFactory(ABC):
    @abstractmethod
    def get_dog(self):
        pass

class CatFactory(ABC):
    @abstractmethod
    def get_cat(self):
        pass

class Poodle(Dog):
    def speak(self):
        return 'Poodle says Woof'
    
class Rottweiler(Dog):
    def speak(self):
        return 'Rottweiler says Wuff'
    

class Persian(Cat):
    def speak(self):
        return 'Persian says Meow'
    
class Siamese(Cat):
    def speak(self):
        return 'Siamese says Meow'
    

class PoodleFactory(DogFactory):
    def get_dog(self):
        return Poodle()
    
class RottweilerFactory(DogFactory):
    def get_dog(self):
        return Rottweiler()
    
