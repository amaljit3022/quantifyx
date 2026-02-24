from quantifyx.exceptions import QuantifyXError


class InvalidFlowRelationInputError(QuantifyXError):
    """Raised when invalid inputs are given to flow relations."""
    pass


def flow_from_area_velocity(area_m2: float, velocity_ms: float) -> float:
    """
    Q = A × V
    Returns flow in m3/s
    """
    if area_m2 <= 0:
        raise InvalidFlowRelationInputError("Area must be positive.")

    if velocity_ms <= 0:
        raise InvalidFlowRelationInputError("Velocity must be positive.")

    return area_m2 * velocity_ms


def velocity_from_flow_area(flow_m3s: float, area_m2: float) -> float:
    """
    V = Q / A
    Returns velocity in m/s
    """
    if flow_m3s <= 0:
        raise InvalidFlowRelationInputError("Flow must be positive.")

    if area_m2 <= 0:
        raise InvalidFlowRelationInputError("Area must be positive.")

    return flow_m3s / area_m2