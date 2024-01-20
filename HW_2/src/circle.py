from math import pi
from HW_2.src.figure import Figure


class Circle(Figure):

    def __init__(self, radius: int):
        if radius <= 0:
            raise ValueError("Радиус круга должен быть числом больше нуля")
        super().__init__(name="Circle")
        self.radius = radius

    def get_area(self):
        return pi * self.radius ** 2

    def get_perimeter(self):
        return 2 * pi * self.radius
