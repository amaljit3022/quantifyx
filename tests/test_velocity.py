import pytest

from quantifyx.units.velocity import to_base, from_base, InvalidVelocityUnitError


def test_velocity_conversion():
    assert round(to_base(36, "kmh"), 2) == 10.00
    assert round(from_base(10, "kmh"), 2) == 36.00


def test_invalid_velocity_unit():
    with pytest.raises(InvalidVelocityUnitError):
        to_base(5, "mph")