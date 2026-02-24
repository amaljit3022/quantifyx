from math import pi

from quantifyx.exceptions import QuantifyXError


class InvalidDimensionError(QuantifyXError):
    """Raised when a geometric dimension is invalid."""
    pass


def circle(radius: float) -> float:
    """
    Calculate the area of a circle.

    Parameters
    ----------
    radius : float
        Radius of the circle (must be positive)

    Returns
    -------
    float
        Area of the circle
    """
    if radius <= 0:
        raise InvalidDimensionError("Radius must be a positive number.")

    return pi * radius ** 2