from lab_python_oop.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, a, figure_color):
        super().__init__(a, a, figure_color)
        self.name = "Квадрат"

    def __repr__(self):
        return '{}\nДлина стороны = {}\nПлощадь фигуры = {}\nЦвет = {}\n' \
            .format(self.name, self.width, self.area(), self.color)
