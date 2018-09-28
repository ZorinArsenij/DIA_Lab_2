from abc import ABC, abstractmethod


class GeometricFigure(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def get_name(self):
        pass
