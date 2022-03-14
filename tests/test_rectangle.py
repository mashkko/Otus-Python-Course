def test_circle_name(rectangle):
    assert rectangle.name == "Прямоугольник"


def test_circle_area(rectangle):
    assert rectangle.area == 200


def tests_circle_perimeter(rectangle):
    assert rectangle.perimeter == 60


def tests_add_square_area_to_circle(square, rectangle):
    assert rectangle.add_area(square) == 300


def tests_send_wrong_figure_to_add_area(rectangle):
    try:
        rectangle.add_area("INVALID_FIGURE")
    except ValueError as exc:
        assert exc.args[0] == "Передан неправильный класс"
