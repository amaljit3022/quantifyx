import pytest

from quantifyx.physics.density import (
    water_density,
    mass_from_density,
    volume_from_density,
    InvalidDensityError,
)


def test_water_density():
    assert water_density() == 1000.0


def test_mass_from_density():
    mass = mass_from_density(2, 1000)
    assert mass == 2000


def test_volume_from_density():
    volume = volume_from_density(2000, 1000)
    assert volume == 2


def test_invalid_density_inputs():
    with pytest.raises(InvalidDensityError):
        mass_from_density(-1, 1000)

    with pytest.raises(InvalidDensityError):
        volume_from_density(1000, 0)