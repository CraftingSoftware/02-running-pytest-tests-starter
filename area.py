"""
Calculate the area of various shapes.
"""
import math


def square(length):
    """
    Calculate the area of a square.

    Args:
        length: Length of the square

    Returns:
        Area of the square
    """
    return length ** 2


def rectangle(length, width):
    """
    Calculate the area of a rectangle.

    Args:
        length: Length of the rectangle
        width: Width of the rectangle

    Returns:
        Area of the rectangle
    """
    return length * width


def parallelogram(base, height):
    """
    Calculate the area of a parallelogram.

    Args:
        base: Base length of the parallelogram
        height: Height of the parallelogram

    Returns:
        Area of the parallelogram
    """
    return base * height


def trapezoid(base_one, base_two, height):
    """
    Calculate the area of a trapezoid.

    Args:
        base: First base length of the trapezoid
        base: Second base length of the trapezoid
        height: Height of the trapezoid

    Returns:
        Area of the trapezoid
    """
    return (height / 2) * (base_one + base_two)


def triangle(base, height):
    """
    Calculate the area of a triangle.

    Args:
        base: Base length of the triangle
        height: Height of the triangle

    Returns:
        Area of the triangle
    """
    return 0.5 * base * height


def circle(radius):
    """
    Calculate the area of a circle.

    Args:
        radius: Radius of the circle

    Returns:
        Area of the circle
    """
    return math.pi * radius ** 2


def ellipse(semi_major, semi_minor):
    """
    Calculate the area of a ellipse.

    Args:
        semi_major: Largest radius of the ellipse
        semi_minor: Smallest radius of the ellipse

    Returns:
        Area of the ellipse
    """
    return math.pi * semi_major * semi_minor
