def test_triangle_name(triangle):
    assert triangle.name == "Треугольник"


def test_triangle_area(triangle):
    assert triangle.area == 9.797958971132712


def tests_triangle_perimeter(triangle):
    assert triangle.perimeter == 16


def tests_add_square_area_to_triangle(square, triangle):
    assert triangle.add_area(square) == 109.797958971132712


def tests_send_wrong_figure_to_add_area(triangle):
    try:
        triangle.add_area("INVALID_FIGURE")
    except ValueError as exc:
        assert exc.args[0] == "Передан неправильный класс"
