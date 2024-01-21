from HW_2.src.figure import Figure

PI: float = 3.14
class Circle(Figure):

    def __init__(self, radius: int):
        if radius <= 0:
            raise ValueError("Радиус круга должен быть числом больше нуля")
        super().__init__(name="Circle")
        self.radius = radius

    def get_area(self):
        return round((PI * self.radius ** 2), 2)

    def get_perimeter(self):
        return round((2 * PI * self.radius), 2)
