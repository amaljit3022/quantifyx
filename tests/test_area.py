import pytest

from quantifyx.geometry.area import circle, InvalidDimensionError


def test_circle_area_valid():
    result = circle(7)
    assert round(result, 2) == 153.94


def test_circle_area_invalid_radius():
    with pytest.raises(InvalidDimensionError):
        circle(-5)