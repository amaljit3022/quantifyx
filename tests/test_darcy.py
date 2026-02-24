import pytest

from quantifyx.physics.darcy import (
    reynolds_number,
    friction_factor_laminar,
    friction_factor_blasius,
    headloss_darcy,
    InvalidDarcyInputError,
)


def test_reynolds_number():
    re = reynolds_number(1, 0.1, 1e-6)
    assert re == pytest.approx(100000, rel=1e-9)


def test_friction_factor_laminar():
    f = friction_factor_laminar(1000)
    assert round(f, 3) == 0.064


def test_friction_factor_blasius():
    f = friction_factor_blasius(100000)
    assert round(f, 4) == 0.0178


def test_headloss():
    # Example controlled scenario
    f = 0.02
    h = headloss_darcy(f, 100, 0.2, 2)
    assert round(h, 2) > 0


def test_invalid_inputs():
    with pytest.raises(InvalidDarcyInputError):
        reynolds_number(-1, 0.1, 1e-6)