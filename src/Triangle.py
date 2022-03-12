# New class declaration
import math

from src.Figure import Figure


class Triangle(Figure):
    def __init__(self, a: int, b: int, c: int):
        if a + b > c and a + c > b and b + c > a:
            self.a = a
            self.b = b
            self.c = c
        else:
            raise ValueError('Треугольника с такими сторонами не существует')

    @property
    def area(self):
        p = self.perimeter / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    @property
    def perimeter(self):
        return self.a + self.b + self.c

    def __repr__(self):
        return "Треугольник. Стороны: {self.a}, {self.b}, {self.c}," \
               " Периметр =  {self.perimeter}, площадь = {self.area}"
