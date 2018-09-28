from lab_python_oop.geometricfigure import GeometricFigure
from lab_python_oop.color import Color
from math import pi


class Circle(GeometricFigure):
    def __init__(self, radius, figure_color):
        self.radius = radius
        self.color = Color(figure_color)
        self.name = "Круг"

    def area(self):
        return self.radius * self.radius * pi

    def get_name(self):
        return self.name

    def __repr__(self):
        return '{}\nРадиус = {}\nПлощадь фигуры = {}\nЦвет = {}\n' \
            .format(self.name, self.radius, self.area(), self.color)
