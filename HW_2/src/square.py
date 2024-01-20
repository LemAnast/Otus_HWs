from HW_2.src.rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, side_a: int):
        if side_a <= 0:
            raise ValueError("Сторона квадрата должна быть числом больше нуля")
        super().__init__(side_a, side_a)
        self.name = "Square"
