import pytest

from quantifyx.geometry.area import circle as area_circle
from quantifyx.geometry.perimeter import circle as perimeter_circle
from quantifyx.exceptions import InvalidDimensionError


def test_circle_area_valid():
    result = area_circle(7)
    assert round(result, 2) == 153.94


def test_circle_perimeter_valid():
    result = perimeter_circle(7)
    assert round(result, 2) == 43.98


def test_circle_invalid_radius():
    with pytest.raises(InvalidDimensionError):
        area_circle(-5)