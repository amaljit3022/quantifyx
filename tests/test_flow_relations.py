import pytest

from quantifyx.physics.flow_relations import (
    flow_from_area_velocity,
    velocity_from_flow_area,
    InvalidFlowRelationInputError,
)


def test_flow_from_area_velocity():
    flow = flow_from_area_velocity(0.5, 2)
    assert flow == 1.0


def test_velocity_from_flow_area():
    velocity = velocity_from_flow_area(1.0, 0.5)
    assert velocity == 2.0


def test_invalid_inputs():
    with pytest.raises(InvalidFlowRelationInputError):
        flow_from_area_velocity(-1, 2)