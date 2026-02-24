from quantifyx.physics.darcy import pipe_headloss


def calculate_pipe_headloss(
    length_m: float,
    diameter_m: float,
    flow_m3s: float,
    roughness_m: float,
    kinematic_viscosity: float,
) -> dict:
    """
    High-level engineering API for pipe headloss.

    This wraps the physics layer and is intended for
    direct use in engineering applications.
    """
    return pipe_headloss(
        length_m=length_m,
        diameter_m=diameter_m,
        flow_m3s=flow_m3s,
        roughness_m=roughness_m,
        kinematic_viscosity=kinematic_viscosity,
    )