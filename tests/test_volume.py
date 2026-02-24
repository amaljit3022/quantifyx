import pytest

from quantifyx.geometry.volume import sphere
from quantifyx.exceptions import InvalidDimensionError


def test_sphere_volume_valid():
    result = sphere(7)
    assert round(result, 2) == 1436.76


def test_sphere_volume_invalid_radius():
    with pytest.raises(InvalidDimensionError):
        sphere(0)