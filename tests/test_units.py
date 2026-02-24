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

from quantifyx.units.area_units import to_base as area_to_base
from quantifyx.units.area_units import from_base as area_from_base
from quantifyx.units.area_units import InvalidAreaUnitError


def test_area_to_base():
    assert area_to_base(1, "hectare") == 10_000
    assert area_to_base(1, "km2") == 1_000_000
    assert round(area_to_base(1, "acre"), 4) == 4046.8564


def test_area_from_base():
    assert area_from_base(10_000, "hectare") == 1
    assert area_from_base(1_000_000, "km2") == 1
    assert round(area_from_base(4046.8564, "acre"), 2) == 1.00


def test_invalid_area_unit():
    with pytest.raises(InvalidAreaUnitError):
        area_to_base(5, "bigha")

from quantifyx.units.volume_units import to_base as volume_to_base
from quantifyx.units.volume_units import from_base as volume_from_base
from quantifyx.units.volume_units import InvalidVolumeUnitError


def test_volume_to_base():
    assert volume_to_base(1, "liter") == 0.001
    assert volume_to_base(1000, "liter") == 1
    assert round(volume_to_base(1, "ft3"), 6) == 0.028317


def test_volume_from_base():
    assert volume_from_base(1, "liter") == 1000
    assert volume_from_base(1, "ml") == 1_000_000
    assert round(volume_from_base(0.003785411784, "gallon_us"), 2) == 1.00


def test_invalid_volume_unit():
    with pytest.raises(InvalidVolumeUnitError):
        volume_to_base(10, "bucket")

from quantifyx.units.mass import to_base as mass_to_base
from quantifyx.units.mass import from_base as mass_from_base
from quantifyx.units.mass import InvalidMassUnitError


def test_mass_to_base():
    assert mass_to_base(1000, "g") == 1
    assert mass_to_base(1, "tonne") == 1000
    assert round(mass_to_base(1, "lb"), 6) == 0.453592


def test_mass_from_base():
    assert mass_from_base(1, "g") == 1000
    assert mass_from_base(1000, "tonne") == 1
    assert round(mass_from_base(0.45359237, "lb"), 2) == 1.00


def test_invalid_mass_unit():
    with pytest.raises(InvalidMassUnitError):
        mass_to_base(5, "stone")