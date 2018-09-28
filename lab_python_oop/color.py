class Color:
    def __init__(self, figure_color):
        self._x = figure_color

    def get_x(self):
        return self._x

    def set_x(self, value):
        self._x = value

    def del_x(self):
        del self._x

    def __str__(self):
        return str(self._x)

    x = property(get_x, set_x, del_x, "I'm color.")