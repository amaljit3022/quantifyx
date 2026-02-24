from math import pi

from quantifyx.exceptions import InvalidDimensionError


def sphere(radius: float) -> float:
    """
    Calculate the volume of a sphere.

    Parameters
    ----------
    radius : float
        Radius of the sphere (must be positive)

    Returns
    -------
    float
        Volume of the sphere
    """
    if radius <= 0:
        raise InvalidDimensionError("Radius must be a positive number.")

    return (4 / 3) * pi * radius ** 3