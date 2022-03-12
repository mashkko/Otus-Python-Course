# New class declaration

from src.Figure import Figure


class Rectangle(Figure):
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    @property
    def area(self):
        return self.a * self.b

    @property
    def perimeter(self):
        return 2 * (self.a + self.b)

    def __repr__(self): return "Прямоугольник. Стороны а = {self.a}, b = {self.b}, периметр = {self.perimeter}, " \
                               "площадь = {self.area} "
