from math import pi

from quantifyx.exceptions import InvalidDimensionError


def circle(radius: float) -> float:
    """
    Calculate the perimeter (circumference) of a circle.

    Parameters
    ----------
    radius : float
        Radius of the circle (must be positive)

    Returns
    -------
    float
        Perimeter of the circle
    """
    if radius <= 0:
        raise InvalidDimensionError("Radius must be a positive number.")

    return 2 * pi * radius