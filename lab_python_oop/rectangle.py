from lab_python_oop.geometricfigure import GeometricFigure
from lab_python_oop.color import Color


class Rectangle(GeometricFigure):
    def __init__(self, width, height, figure_color):
        self.width = width
        self.height = height
        self.color = Color(figure_color)
        self.name = "Прямоугольник"

    def area(self):
        return self.width * self.height

    def get_name(self):
        return self.name

    def __repr__(self):
        return '{}\nШирина = {}\nВысота = {}\nПлощадь фигуры = {}\nЦвет = {}\n' \
            .format(self.name, self.width, self.height, self.area(), self.color)