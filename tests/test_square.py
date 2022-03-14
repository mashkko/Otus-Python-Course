def test_circle_name(square):
    assert square.name == "Квадрат"


def test_circle_area(square):
    assert square.area == 100


def tests_circle_perimeter(square):
    assert square.perimeter == 40


def tests_add_square_area_to_circle(circle, square):
    assert square.add_area(circle) == 414.1592653589793


def tests_send_wrong_figure_to_add_area(square):
    try:
        square.add_area("INVALID_FIGURE")
    except ValueError as exc:
        assert exc.args[0] == "Передан неправильный класс"
