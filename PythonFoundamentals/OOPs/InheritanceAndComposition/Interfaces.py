# Interface is like promise to provide certain kind of behaviour

from abc import ABC, abstractclassmethod


class JSONify(ABC):
    @abstractclassmethod
    def toJSON(self):
        pass


class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractclassmethod
    def calcArea(self):
        pass

# now we have promised this method to have JSONify if not implement it throws this error
# TypeError: Can't instantiate abstract class GraphicShape with abstract method calcArea
class Circle(GraphicShape, JSONify):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return 3.14 * (self.radius ** 2)

    def toJSON(self):
        return f"{{\" circle\": {str(self.calcArea())} }}"


class Square(GraphicShape):
    def __init__(self, side):
        self.side = side

    def calcArea(self):
        return self.side * self.side


# g = GraphicShape()

c = Circle(10)
print(c.calcArea())
print(c.toJSON())
