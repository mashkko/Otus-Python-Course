# New class declaration
import math


class Triangle:
    from src.Figure import Figure

    class Triangle(Figure):
        def __init__(self, a: int, b: int, c: int):
            self.a = a
            self.b = b
            self.c = c

        @property
        def area(self):
            p = self.perimeter / 2
            return int(math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c)))

        @property
        def perimetr(self):
            return self.a + self.b + self.c

        def __repr__(self):
            return "Треугольник. Стороны: {self.a}, {self.b}, {self.c}," \
                   " Периметр =  {self.perimeter}, площадь = {self.area}"
