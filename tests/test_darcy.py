import pytest
from quantifyx.physics.darcy import friction_factor_colebrook
from quantifyx.physics.darcy import friction_factor_auto

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

def test_colebrook_smooth_pipe():
    # Example: Re = 100000, smooth pipe (roughness ~ 0)
    f = friction_factor_colebrook(100000, 0.2, 0.000001)
    assert f == pytest.approx(0.018, rel=0.05)

def test_auto_laminar():
    f = friction_factor_auto(1000, 0.1)
    assert f == pytest.approx(0.064, rel=1e-3)


def test_auto_turbulent_smooth():
    f = friction_factor_auto(100000, 0.1, 0)
    assert f == pytest.approx(0.018, rel=0.1)


def test_auto_turbulent_rough():
    f = friction_factor_auto(100000, 0.2, 0.0002)
    assert f > 0