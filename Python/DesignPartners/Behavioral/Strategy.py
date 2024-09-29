# Strategy Pattern: This pattern is used to define a family of algorithms, encapsulate each one, and make them interchangeable. Strategy lets the algorithm vary independently from clients that use it.
# Problem: How to define a family of algorithms, encapsulate each one, and make them interchangeable?
# Solution: The Strategy Pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable.

from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def execute(self):
        pass


class Add(Strategy):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        return self.a + self.b


class Subtract(Strategy):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        return self.a - self.b


class Multiply(Strategy):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        return self.a * self.b


class Context:  
    def __init__(self, strategy):
        self.strategy = strategy

    def execute_strategy(self):
        return self.strategy.execute()


# Usage
add_strategy = Add(3, 4)
context = Context(add_strategy)
print(context.execute_strategy())# 7

subtract_strategy = Subtract(3, 4)
context = Context(subtract_strategy)
print(context.execute_strategy())# -1
