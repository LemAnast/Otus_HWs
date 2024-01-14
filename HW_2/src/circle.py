from HW_2.src.figure import Figure


class Circle(Figure):

    def __init__(self, side_a: int):
        super().__init__(side_a)
        if side_a <= 0:
            raise ValueError("Радиус круга должен быть числом больше нуля")

