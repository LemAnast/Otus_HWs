from HW_2.src.figure import Figure


class Triangle(Figure):

    def __init__(self, side_a: int, side_b: int, side_c: int):
        if side_a <= 0 or side_b <= 0 or side_c <=0:
            raise ValueError("Стороны треугольника должны быть числами больше нуля")
        if not (side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a):
            raise ValueError("Треугольник с такими сторонами не существует")
        super().__init__(name="Triangle")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def get_area(self):
        pass

    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c
