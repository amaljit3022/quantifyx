from quantifyx.exceptions import QuantifyXError


class InvalidAreaUnitError(QuantifyXError):
    """Raised when an unsupported area unit is requested."""
    pass


# Conversion factors to square meters
_AREA_FACTORS = {
    "m2": 1.0,
    "km2": 1_000_000.0,
    "cm2": 0.0001,
    "hectare": 10_000.0,
    "acre": 4046.8564224,
}


def to_base(value: float, unit: str) -> float:
    """
    Convert an area value to square meters.

    Parameters
    ----------
    value : float
        Numerical value
    unit : str
        Unit of the area

    Returns
    -------
    float
        Area in square meters
    """
    if unit not in _AREA_FACTORS:
        raise InvalidAreaUnitError(f"Unsupported area unit: {unit}")

    return value * _AREA_FACTORS[unit]


def from_base(value: float, unit: str) -> float:
    """
    Convert an area value from square meters to another unit.

    Parameters
    ----------
    value : float
        Area in square meters
    unit : str
        Target unit

    Returns
    -------
    float
        Converted area
    """
    if unit not in _AREA_FACTORS:
        raise InvalidAreaUnitError(f"Unsupported area unit: {unit}")

    return value / _AREA_FACTORS[unit]