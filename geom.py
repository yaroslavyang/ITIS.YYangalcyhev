import math
from abc import ABC, abstractmethod

class GeomFigure(ABC):
    @abstractmethod
    def get_area(self):
        pass
    @abstractmethod
    def get_perimeter(self):
        pass

class Circle(GeomFigure):
    def __init__(self, x=0, y=0, r=0):
        self.x = x
        self.y = y
        self.r = r
    def get_area(self):
        return math.pi * self.r ** 2
    def get_perimeter(self):
        return 2 * math.pi * self.r

class Quadrangle(GeomFigure, ABC):
    @abstractmethod
    def get_len(self, x1=0, y1=0, x2=0, y2=0):
        pass

class Rectangle(Quadrangle):
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    def get_len(self, p1, p2):
        return abs(p2 - p1)
    def get_area(self):
        return self.get_len(self.x2, self.x1) * self.get_len(self.y2, self.y1)
    def get_perimeter(self):
        return 2 * (self.get_len(self.x2, self.x1) + self.get_len(self.y2, self.y1))

class Trapezoid(Quadrangle):
    def __init__(self,  x1, y1, x2, y2, x3, y3, x4, y4):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4
    def get_len(self, x1, y1, x2, y2):
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    def get_area(self):
        return (abs(self.x2 - self.x1) + abs(self.x4 - self.x3)) / 2 * (abs(self.y4-self.y1))
    def get_perimeter(self):
        return self.get_len(self.x1, self.y1, self.x2, self.y2) + \
               self.get_len(self.x2, self.y2, self.x3, self.y3) + \
               self.get_len(self.x3, self.y3, self.x4, self.y4) + \
               self.get_len(self.x4, self.y4, self.x1, self.y1)

class Parallelogram(Quadrangle):
    def __init__(self,  x1, y1, x2, y2, x3, y3, x4, y4):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4
    def get_len(self, x1, y1, x2, y2):
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    def get_area(self):
        return abs(self.x1 - self.x2) * abs(self.y1 - self.y4)

    def get_perimeter(self):
        return 2 * (abs(self.x1 - self.x2) + self.get_len(self.x1, self.y1, self.x4, self.y4))

circle = Circle(0, 0, 3)
print(circle.get_area())
print(circle.get_perimeter())
print()
rectangle = Rectangle(0, 0, 3, 3)
print(rectangle.get_area())
print(rectangle.get_perimeter())
print()
trapezoid = Trapezoid(0, 0, 10, 0, 8, 5, 2, 5)
print(trapezoid.get_area())
print(trapezoid.get_perimeter())
print()
parallelogram = Parallelogram(0, 0, 8, 0, 10, 6, 2, 6)
print(parallelogram.get_area())
print(parallelogram.get_perimeter())
print()
