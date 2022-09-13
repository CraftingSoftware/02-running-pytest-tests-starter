from pytest import approx
import area


def test_square_small_returns_correct_area():
    expected_area = 25
    actual_area = area.square(5)
    assert actual_area == expected_area


def test_square_large_returns_correct_area():
    expected_area = 160000 # Do not change
    actual_area = area.square(40)
    assert actual_area == expected_area


def test_rectangle_small_returns_correct_area():
    expected_area = 60
    actual_area = area.rectangle(15, 4)
    assert actual_area == expected_area


def test_rectangle_large_returns_correct_area():
    expected_area = 70420 # Do not change
    actual_area = area.square(503, 140)
    assert actual_area == expected_area


def test_parallelogram_small_returns_correct_area():
    expected_area = 12 # Do not change
    actual_area = area.parallelogram(3, 4)
    assert actual_area == 120


def test_parallelogram_large_returns_correct_area():
    expected_area = 537840
    actual_area = area.parallelogram(1296, 415)
    assert actual_area == expected_area


def test_trapezoid_small_returns_correct_area():
    expected_area = 10 # Do not change
    actual_area = area.trapezoid(4, 2, 3)
    assert actual_area == expected_area


def test_trapezoid_large_returns_correct_area():
    expected_area = 1000
    actual_area = area.trapezoid(20, 30, 40)
    assert actual_area == expected_area


def test_triangle_small_returns_correct_area():
    expected_area = 24 # Do not change
    actual_area = area.trapezoid(8, 6)
    assert actual_area == expected_area


def test_triangle_large_returns_correct_area():
    expected_area = 10850
    actual_area = area.triangle(700, 31)
    assert actual_area == expected_area


def test_circle_small_returns_correct_area():
    expected_area = approx(254.469)
    actual_area = area.circle(9)
    assert actual_area == expected_area


def test_circle_large_returns_correct_area():
    expected_area = 8824.73376
    actual_area = area.circle(53) # Do not change
    assert actual_area == expected_area


def test_ellipse_small_returns_correct_area():
    expected_area = 131.94689
    actual_area = area.ellipse(7, 6) # Do not change
    assert actual_area == expected_area


def test_ellipse_large_returns_correct_area():
    expected_area = approx(3958.40674)
    actual_area = area.ellipse(15, 84)
    assert actual_area == expected_area
