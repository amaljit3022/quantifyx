from quantifyx.exceptions import QuantifyXError


class InvalidUnitError(QuantifyXError):
    """Raised when an unsupported unit is requested."""
    pass


# Conversion factors to meters
_LENGTH_FACTORS = {
    "m": 1.0,
    "km": 1000.0,
    "cm": 0.01,
    "mm": 0.001,
    "inch": 0.0254,
    "ft": 0.3048,
}


def to_base(value: float, unit: str) -> float:
    """
    Convert a length value to meters.

    Parameters
    ----------
    value : float
        Numerical value
    unit : str
        Unit of the value

    Returns
    -------
    float
        Value in meters
    """
    if unit not in _LENGTH_FACTORS:
        raise InvalidUnitError(f"Unsupported length unit: {unit}")

    return value * _LENGTH_FACTORS[unit]


def from_base(value: float, unit: str) -> float:
    """
    Convert a length value from meters to another unit.

    Parameters
    ----------
    value : float
        Value in meters
    unit : str
        Target unit

    Returns
    -------
    float
        Converted value
    """
    if unit not in _LENGTH_FACTORS:
        raise InvalidUnitError(f"Unsupported length unit: {unit}")

    return value / _LENGTH_FACTORS[unit]