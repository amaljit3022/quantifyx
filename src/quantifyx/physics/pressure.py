from quantifyx.exceptions import QuantifyXError
from quantifyx.physics.density import water_density


class InvalidPressureUnitError(QuantifyXError):
    """Raised when an unsupported pressure unit is requested."""
    pass


class InvalidPressureInputError(QuantifyXError):
    """Raised when invalid pressure/head inputs are given."""
    pass


_GRAVITY = 9.80665  # m/s2


# Conversion factors to Pascal
_PRESSURE_FACTORS = {
    "pa": 1.0,
    "kpa": 1000.0,
    "bar": 100000.0,
}


def to_base(value: float, unit: str) -> float:
    """
    Convert pressure value to Pascal.
    """
    if unit not in _PRESSURE_FACTORS:
        raise InvalidPressureUnitError(f"Unsupported pressure unit: {unit}")

    return value * _PRESSURE_FACTORS[unit]


def from_base(value: float, unit: str) -> float:
    """
    Convert pressure value from Pascal.
    """
    if unit not in _PRESSURE_FACTORS:
        raise InvalidPressureUnitError(f"Unsupported pressure unit: {unit}")

    return value / _PRESSURE_FACTORS[unit]


def head_to_pressure(head_m: float, density: float | None = None) -> float:
    """
    Convert head (m) to pressure (Pa).
    Default density is water.
    """
    if head_m <= 0:
        raise InvalidPressureInputError("Head must be positive.")

    rho = density if density is not None else water_density()

    return rho * _GRAVITY * head_m


def pressure_to_head(pressure_pa: float, density: float | None = None) -> float:
    """
    Convert pressure (Pa) to head (m).
    Default density is water.
    """
    if pressure_pa <= 0:
        raise InvalidPressureInputError("Pressure must be positive.")

    rho = density if density is not None else water_density()

    return pressure_pa / (rho * _GRAVITY)