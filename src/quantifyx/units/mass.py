from quantifyx.exceptions import QuantifyXError


class InvalidMassUnitError(QuantifyXError):
    """Raised when an unsupported mass unit is requested."""
    pass


# Conversion factors to kilograms
_MASS_FACTORS = {
    "kg": 1.0,
    "g": 0.001,
    "mg": 0.000001,
    "tonne": 1000.0,
    "lb": 0.45359237,
}


def to_base(value: float, unit: str) -> float:
    """
    Convert a mass value to kilograms.

    Parameters
    ----------
    value : float
        Numerical value
    unit : str
        Unit of mass

    Returns
    -------
    float
        Mass in kilograms
    """
    if unit not in _MASS_FACTORS:
        raise InvalidMassUnitError(f"Unsupported mass unit: {unit}")

    return value * _MASS_FACTORS[unit]


def from_base(value: float, unit: str) -> float:
    """
    Convert a mass value from kilograms to another unit.

    Parameters
    ----------
    value : float
        Mass in kilograms
    unit : str
        Target unit

    Returns
    -------
    float
        Converted mass
    """
    if unit not in _MASS_FACTORS:
        raise InvalidMassUnitError(f"Unsupported mass unit: {unit}")

    return value / _MASS_FACTORS[unit]