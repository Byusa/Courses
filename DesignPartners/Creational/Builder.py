# Builder Parttern: this pattern is used to construct a complex object step by step and the final step will return the object.
# Problem: How to construct a complex object step by step?
# Solution: The Builder Pattern constructs a complex object step by step.

class Builder:
    def __init__(self):
        self.name = None
        self.age = None

    def set_name(self, name):
        self.name = name
        return self

    def set_age(self, age):
        self.age = age
        return self

    def build(self):
        return Person(self)


class Person:
    def __init__(self, builder):
        self.name = builder.name
        self.age = builder.age
        
    def __str__(self):
        return f'{self.name} {self.age}'


# Usage
builder = Builder()
person = builder.set_name('John').set_age(20).build()


print(person) # John 20