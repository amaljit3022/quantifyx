import pytest

from quantifyx.physics.pressure import (
    to_base,
    from_base,
    head_to_pressure,
    pressure_to_head,
    InvalidPressureUnitError,
)


def test_pressure_unit_conversion():
    assert to_base(1, "bar") == 100000
    assert from_base(100000, "bar") == 1


def test_head_pressure_relation():
    # 10 m head of water ≈ 98,066.5 Pa
    pressure = head_to_pressure(10)
    assert round(pressure, 1) == 98066.5

    head = pressure_to_head(pressure)
    assert round(head, 2) == 10.00


def test_invalid_pressure_unit():
    with pytest.raises(InvalidPressureUnitError):
        to_base(5, "psi")