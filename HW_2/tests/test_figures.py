import pytest

from HW_2.src.circle import Circle
from HW_2.src.rectangle import Rectangle
from HW_2.src.square import Square
from HW_2.src.triangle import Triangle


@pytest.mark.figures
@pytest.mark.parametrize("value", ["circle+rect", "rect+square", "square+triangle", "triangle+circle"],
                         ids=["circle+rect", "rect+square", "square+triangle", "triangle+circle"])
def test_add_figure_positive(add_figures, value):
    a, b, summ = add_figures(value=value)
    assert a.add_area(b) == summ, f"Сумма площадей {a.name} и {b.name} не верна"

@pytest.mark.rectangle
@pytest.mark.parametrize("value", ["int", "float"], ids=["int values", "float values"])
def test_create_rectangle_positive(create_rectangle, value):
    a, b = create_rectangle(value=value)
    r = Rectangle(a, b)
    assert isinstance(r, Rectangle), f"Прямоугольник со сторонами {a} и {b} не создан"


@pytest.mark.rectangle
@pytest.mark.parametrize("value", ["negative"], ids=["negative values"])
def test_create_rectangle_negative(create_rectangle, value):
    a, b = create_rectangle(value=value)
    with pytest.raises(ValueError, match="Стороны прямоугольника должны быть числом больше нуля"):
        Rectangle(a, b)


@pytest.mark.rectangle
@pytest.mark.parametrize("value", ["int", "float"], ids=["int values", "float values"])
def test_rectangle_perimeter(rectangle_perimeter, value):
    a, b, perimeter = rectangle_perimeter(value=value)
    r = Rectangle(a, b)
    assert r.get_perimeter() == perimeter, f"Периметр прямоугольника со сторонами {a} и {b} не верен"


@pytest.mark.rectangle
@pytest.mark.parametrize("value", ["int", "float"], ids=["int values", "float values"])
def test_rectangle_area(rectangle_area, value):
    a, b, area = rectangle_area(value=value)
    r = Rectangle(a, b)
    assert r.get_area() == area, f"Площадь прямоугольника со сторонами {a} и {b} не верна"


@pytest.mark.square
@pytest.mark.parametrize("side_a", [5, 1.5], ids=["int values", "float values"])
def test_create_square_positive(side_a):
    r = Square(side_a)
    assert isinstance(r, Square), f"Квадрат со сторонами {side_a} не создан"


@pytest.mark.square
@pytest.mark.parametrize("side_a", [-5, -1.5], ids=["int values", "float values"])
def test_create_square_negative(side_a):
    with pytest.raises(ValueError, match="Сторона квадрата должна быть числом больше нуля"):
        Square(side_a)


@pytest.mark.square
@pytest.mark.parametrize(("side_a", "perimeter"), [(5, 20), (1.5, 6)], ids=["int values", "float values"])
def test_square_perimeter(side_a, perimeter):
    s = Square(side_a)
    assert s.get_perimeter() == perimeter, f"Периметр квадрата со стороной {side_a} не верен"


@pytest.mark.square
@pytest.mark.parametrize(("side_a", "area"), [(5, 25), (1.5, 2.25)], ids=["int values", "float values"])
def test_square_area(side_a, area):
    s = Square(side_a)
    assert s.get_area() == area, f"Площадь квадрата со стороной {side_a} не верна"


@pytest.mark.triangle
@pytest.mark.parametrize("value", ["int", "float"], ids=["int values", "float values"])
def test_create_triangle_positive(create_triangle, value):
    a, b, c = create_triangle(value=value)
    t = Triangle(a, b, c)
    assert isinstance(t, Triangle), f"Треугольник со сторонами {a}, {b} и {c} не создан"


@pytest.mark.triangle
@pytest.mark.parametrize("value", ["negative"], ids=["negative values"])
def test_create_triangle_negative(create_triangle, value):
    a, b, c = create_triangle(value=value)
    with pytest.raises(ValueError, match="Стороны треугольника должны быть числами больше нуля"):
        Triangle(a, b, c)


@pytest.mark.triangle
@pytest.mark.parametrize("value", ["nonexist"], ids=["nonexist values"])
def test_create_triangle_nonexist(create_triangle, value):
    a, b, c = create_triangle(value=value)
    with pytest.raises(ValueError, match="Треугольник с такими сторонами не существует"):
        Triangle(a, b, c)


@pytest.mark.triangle
@pytest.mark.parametrize("value", ["int", "float"], ids=["int values", "float values"])
def test_triangle_perimeter(triangle_perimeter, value):
    a, b, c, perimeter = triangle_perimeter(value=value)
    t = Triangle(a, b, c)
    assert t.get_perimeter() == perimeter, f"Периметр треугольника со сторонами {a}, {b} и {c} не верен"


@pytest.mark.triangle
@pytest.mark.parametrize("value", ["int", "float"], ids=["int values", "float values"])
def test_triangle_area(triangle_area, value):
    a, b, c, area = triangle_area(value=value)
    t = Triangle(a, b, c)
    assert t.get_area() == area, f"Площадь треугольника со сторонами {a}, {b} и {c} не верна"


@pytest.mark.circle
@pytest.mark.parametrize("radius", [3, 5], ids=["int values", "float values"])
def test_create_circle_positive(radius):
    c = Circle(radius)
    assert isinstance(c, Circle), f"Круг радиусом {radius} не создан"


@pytest.mark.circle
@pytest.mark.parametrize("radius", [-3, -5], ids=["int values", "float values"])
def test_create_circle_negative(radius):
    with pytest.raises(ValueError, match="Радиус круга должен быть числом больше нуля"):
        Circle(radius)


@pytest.mark.circle
@pytest.mark.parametrize(("radius", "perimeter"), [(5, 31.4), (1.5, 9.42)], ids=["int values", "float values"])
def test_circle_perimeter(radius, perimeter):
    c = Circle(radius)
    assert c.get_perimeter() == perimeter, f"Периметр круга с радиусом {radius} не верен"


@pytest.mark.circle
@pytest.mark.parametrize(("radius", "area"), [(5, 78.5), (1.5, 7.07)], ids=["int values", "float values"])
def test_circle_area(radius, area):
    c = Circle(radius)
    assert c.get_area() == area, f"Площадь круга с радиусом {radius} не верна"
