from quantifyx.physics.darcy import pipe_headloss
from quantifyx.hydraulics.materials import get_roughness


def calculate_pipe_headloss(
    length_m: float,
    diameter_m: float,
    flow_m3s: float,
    kinematic_viscosity: float,
    material: str | None = None,
    roughness_m: float | None = None,
) -> dict:
    """
    High-level engineering API for pipe headloss.

    User may specify:
    - material (preferred)
    OR
    - roughness directly
    """

    if material:
        roughness = get_roughness(material)
    elif roughness_m is not None:
        roughness = roughness_m
    else:
        raise ValueError("Either material or roughness_m must be provided.")

    return pipe_headloss(
        length_m=length_m,
        diameter_m=diameter_m,
        flow_m3s=flow_m3s,
        roughness_m=roughness,
        kinematic_viscosity=kinematic_viscosity,
    )