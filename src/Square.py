# New class declaration
from src.Figure import Figure


class Square(Figure):
    def __init__(self, a: int):
        self.a = a

    @property
    def area(self):
        return self.a ** 2

    @property
    def perimeter(self):
        return self.a * 4

    def __repr__(self):
        return "Квадрат. Сторона = {self.a}, периметр = {self.perimeter}, площадь = {self.area}"
