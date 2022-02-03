# New class declaration
class Figure:
    def __init__(self, name: str):
        self.f_name = name
        self.f_area = 0
        self.f_perimeter = 0

# Вычисление суммы фигур
    def add_area(self, figure):
        if isinstance(figure, Figure):
            return figure.area + self.area
        else:
            raise ValueError("передан неправильный класс")

    @property
    def name(self):
        return self.f_name

    @property
    def area(self):
        return self.f_area

    @property
    def perimeter(self):
        return self.f_perimeter

    @name.setting
    def name(self, value):
        self.f_name = value

    @area.setter
    def area(self, value):
        self.f_area = value

    @perimeter.setter
    def perimeter(self, value):
        self.f_perimeter = value
