# Factory Pattern: This pattern is used to create an object without exposing the creation logic to the client and refer to a newly created object using a common interface.
# Problem: How to create an object without exposing the creation logic to the client and refer to a newly created object using a common interface?
# Solution: The Factory Pattern creates an object without exposing the creation logic to the client and refers to a newly created object using a common interface.

class Dog:
    def __init__(self):
        self.name = 'Dog'
        self.sound = 'Bark'
        
    def speak(self):
        return f'{self.name} says {self.sound}'
    
class Cat:
    def __init__(self):
        self.name = 'Cat'
        self.sound = 'Meow'
        
    def speak(self):
        return f'{self.name} says {self.sound}'
    
class AnimalFactory:
    def get_animal(self, animal):
        if animal == 'Dog':
            return Dog()
        if animal == 'Cat':
            return Cat()
        raise ValueError('Invalid animal')
    
# Usage
animal_factory = AnimalFactory()
dog = animal_factory.get_animal('Dog')
print(dog.speak()) # Dog says Bark