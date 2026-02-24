import pytest

from quantifyx.hydraulics.materials import get_roughness, InvalidMaterialError
from quantifyx.hydraulics.pipe import calculate_pipe_headloss


def test_material_lookup():
    assert get_roughness("hdpe") > 0


def test_invalid_material():
    with pytest.raises(InvalidMaterialError):
        get_roughness("wood")


def test_pipe_api_with_material():
    result = calculate_pipe_headloss(
        length_m=100,
        diameter_m=0.2,
        flow_m3s=0.01,
        kinematic_viscosity=1e-6,
        material="hdpe",
    )

    assert result["headloss"] > 0