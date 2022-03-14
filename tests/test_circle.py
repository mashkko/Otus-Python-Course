def test_circle_name(circle):
    assert circle.name == "Круг"


def test_circle_area(circle):
    assert circle.area == 314.1592653589793


def tests_circle_perimeter(circle):
    assert circle.perimeter == 62.83185307179586


def tests_add_square_area_to_circle(square, circle):
    assert circle.add_area(square) == 414.1592653589793


def tests_send_wrong_figure_to_add_area(circle):
    try:
        circle.add_area("INVALID_FIGURE")
    except ValueError as exc:
        assert exc.args[0] == "Передан неправильный класс"
