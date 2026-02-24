import pytest

from quantifyx.units.length import to_base, from_base, InvalidUnitError


def test_length_to_base():
    assert to_base(1, "km") == 1000
    assert to_base(100, "cm") == 1
    assert round(to_base(12, "inch"), 4) == 0.3048


def test_length_from_base():
    assert from_base(1000, "km") == 1
    assert from_base(1, "cm") == 100
    assert round(from_base(0.3048, "inch"), 2) == 12


def test_invalid_length_unit():
    with pytest.raises(InvalidUnitError):
        to_base(10, "yard")