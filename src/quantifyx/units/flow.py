from quantifyx.exceptions import QuantifyXError


class InvalidFlowUnitError(QuantifyXError):
    """Raised when an unsupported flow unit is requested."""
    pass


# Conversion factors to m3/s
_FLOW_FACTORS = {
    "m3s": 1.0,
    "lps": 0.001,
    "lpm": 0.001 / 60,
    "cmd": 1 / 86400,
    "mld": 1000 / 86400,  # 1 MLD = 1000 m3/day
}


def to_base(value: float, unit: str) -> float:
    """
    Convert flow value to cubic meters per second (m3/s).
    """
    if unit not in _FLOW_FACTORS:
        raise InvalidFlowUnitError(f"Unsupported flow unit: {unit}")

    return value * _FLOW_FACTORS[unit]


def from_base(value: float, unit: str) -> float:
    """
    Convert flow value from m3/s to target unit.
    """
    if unit not in _FLOW_FACTORS:
        raise InvalidFlowUnitError(f"Unsupported flow unit: {unit}")

    return value / _FLOW_FACTORS[unit]