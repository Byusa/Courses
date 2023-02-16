# abstract base classes =  other base class (for inherit)
#  1. not allow cosumer to create instances of itself but implement)
#  2. enforce the constrain that some methods that sub classes can implemet

from abc import ABC, abstractclassmethod


class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractclassmethod
    def calcArea(self):
        pass


class Circle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return 3.14 * (self.radius ** 2)


class Square(GraphicShape):
    def __init__(self, side):
        self.side = side

    def calcArea(self):
        return self.side * self.side


g = GraphicShape()

c = Circle(10)
print(c.calcArea())
s = Square(12)
print(s.calcArea())
