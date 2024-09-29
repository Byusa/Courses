# Singleton Pattern: This parttern ensures that a class has only one instance and provides a global point of access to it.
# Problem: How to ensure that a class has only one instance and provide a global point of access to it?
# Solution: The Singleton Pattern ensures that a class has only one instance and provides a global point of access to it.

class Singleton:
    __instance = None

    def __new__(cls):
        if cls._instance is None:
            print('Creating the object')
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance
    
# - both are same objects
# Usage

singleton1 = Singleton()
print(singleton1)
singleton2 = Singleton()
print(singleton2)

print(singleton1 == singleton2) # True 