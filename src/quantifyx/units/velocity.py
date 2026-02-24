from quantifyx.exceptions import QuantifyXError


class InvalidVelocityUnitError(QuantifyXError):
    """Raised when an unsupported velocity unit is requested."""
    pass


# Conversion factors to m/s
_VELOCITY_FACTORS = {
    "ms": 1.0,
    "kmh": 1000 / 3600,
    "fps": 0.3048,
}


def to_base(value: float, unit: str) -> float:
    """
    Convert velocity to m/s.
    """
    if unit not in _VELOCITY_FACTORS:
        raise InvalidVelocityUnitError(f"Unsupported velocity unit: {unit}")

    return value * _VELOCITY_FACTORS[unit]


def from_base(value: float, unit: str) -> float:
    """
    Convert velocity from m/s.
    """
    if unit not in _VELOCITY_FACTORS:
        raise InvalidVelocityUnitError(f"Unsupported velocity unit: {unit}")

    return value / _VELOCITY_FACTORS[unit]