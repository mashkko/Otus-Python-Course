# New class declaration
import math


class Circle:
    from src.Figure import Figure

    class Circle(Figure):
        def __init__(self, r: int):
            self.r = r

        @property
        def area(self):
            return math.pi * (self.r ** 2)

        @property
        def perimeter(self):
            return 2 * math.pi * self.r

        def __repr__(self):
            return "Круг. Радиус = {self.r} периметр = {self.perimeter}, площад = {self.area}"
