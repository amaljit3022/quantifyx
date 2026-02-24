from quantifyx.exceptions import QuantifyXError


class InvalidVolumeUnitError(QuantifyXError):
    """Raised when an unsupported volume unit is requested."""
    pass


# Conversion factors to cubic meters
_VOLUME_FACTORS = {
    "m3": 1.0,
    "liter": 0.001,
    "ml": 0.000001,
    "km3": 1_000_000_000.0,
    "ft3": 0.028316846592,
    "gallon_us": 0.003785411784,
}


def to_base(value: float, unit: str) -> float:
    """
    Convert a volume value to cubic meters.

    Parameters
    ----------
    value : float
        Numerical value
    unit : str
        Unit of volume

    Returns
    -------
    float
        Volume in cubic meters
    """
    if unit not in _VOLUME_FACTORS:
        raise InvalidVolumeUnitError(f"Unsupported volume unit: {unit}")

    return value * _VOLUME_FACTORS[unit]


def from_base(value: float, unit: str) -> float:
    """
    Convert a volume value from cubic meters to another unit.

    Parameters
    ----------
    value : float
        Volume in cubic meters
    unit : str
        Target unit

    Returns
    -------
    float
        Converted volume
    """
    if unit not in _VOLUME_FACTORS:
        raise InvalidVolumeUnitError(f"Unsupported volume unit: {unit}")

    return value / _VOLUME_FACTORS[unit]