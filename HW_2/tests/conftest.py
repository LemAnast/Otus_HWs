import pytest

from HW_2.src.circle import Circle
from HW_2.src.rectangle import Rectangle
from HW_2.src.square import Square
from HW_2.src.triangle import Triangle


@pytest.fixture()
def add_figures():
    def _wrapper(value: str):
        if value == "circle+rect":
            return Circle(5), Rectangle(4, 5), 98.5
        elif value == "rect+square":
            return Rectangle(4, 5), Square(5), 45
        elif value == "square+triangle":
            return Square(5), Triangle(3, 4, 5), 31
        elif value == "triangle+circle":
            return Triangle(3, 4, 5), Circle(5), 84.5
        else:
            raise AssertionError("Только определенные суммы: circle+rect, rect+square, square+triangle, triangle+circle")
    yield _wrapper


@pytest.fixture()
def create_rectangle():
    def _wrapper(value: str):
        if value == "int":
            return 3, 5
        elif value == "float":
            return 3.5, 5.5
        elif value == "negative":
            return -3, -5
        else:
            raise AssertionError("Только int, float, negative")
    yield _wrapper


@pytest.fixture()
def rectangle_perimeter():
    def _wrapper(value: str):
        if value == "int":
            return 3, 5, 16
        elif value == "float":
            return 3.5, 5.5, 18
        else:
            raise AssertionError("Только int, float")
    yield _wrapper


@pytest.fixture()
def rectangle_area():
    def _wrapper(value: str):
        if value == "int":
            return 3, 5, 15
        elif value == "float":
            return 3.5, 5.5, 19.25
        else:
            raise AssertionError("Только int, float")
    yield _wrapper


@pytest.fixture()
def create_triangle():
    def _wrapper(value: str):
        if value == "int":
            return 3, 4, 5
        elif value == "float":
            return 3.5, 4.5, 5.5
        elif value == "nonexist":
            return 1, 2, 6
        elif value == "negative":
            return -3, -4, -5
        else:
            raise AssertionError("Только int, float, non-exist, negative")
    yield _wrapper


@pytest.fixture()
def triangle_perimeter():
    def _wrapper(value: str):
        if value == "int":
            return 3, 4, 5, 12
        elif value == "float":
            return 3.5, 4.5, 5.5, 13.5
        else:
            raise AssertionError("Только int, float")
    yield _wrapper


@pytest.fixture()
def triangle_area():
    def _wrapper(value: str):
        if value == "int":
            return 3, 4, 5, 36
        elif value == "float":
            return 3.5, 3.5, 4.0, 33
        else:
            raise AssertionError("Только int, float")
    yield _wrapper