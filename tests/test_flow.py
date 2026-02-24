import pytest

from quantifyx.units.flow import to_base, from_base, InvalidFlowUnitError


def test_flow_to_base():
    assert to_base(1000, "lps") == 1
    assert round(to_base(1, "mld"), 6) == round(1000 / 86400, 6)


def test_flow_from_base():
    assert from_base(1, "lps") == 1000
    assert round(from_base(1000 / 86400, "mld"), 2) == 1.00


def test_invalid_flow_unit():
    with pytest.raises(InvalidFlowUnitError):
        to_base(5, "cusec")