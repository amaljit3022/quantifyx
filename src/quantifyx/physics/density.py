from quantifyx.exceptions import QuantifyXError


class InvalidDensityError(QuantifyXError):
    """Raised when density value is invalid."""
    pass


# Standard density values (kg/m3)
_WATER_DENSITY = 1000.0  # kg/m3 at ~4°C


def water_density() -> float:
    """
    Return standard water density in kg/m3.
    """
    return _WATER_DENSITY


def mass_from_density(volume_m3: float, density: float) -> float:
    """
    Calculate mass from volume and density.

    Parameters
    ----------
    volume_m3 : float
        Volume in cubic meters
    density : float
        Density in kg/m3

    Returns
    -------
    float
        Mass in kilograms
    """
    if volume_m3 <= 0:
        raise InvalidDensityError("Volume must be positive.")

    if density <= 0:
        raise InvalidDensityError("Density must be positive.")

    return volume_m3 * density


def volume_from_density(mass_kg: float, density: float) -> float:
    """
    Calculate volume from mass and density.

    Parameters
    ----------
    mass_kg : float
        Mass in kilograms
    density : float
        Density in kg/m3

    Returns
    -------
    float
        Volume in cubic meters
    """
    if mass_kg <= 0:
        raise InvalidDensityError("Mass must be positive.")

    if density <= 0:
        raise InvalidDensityError("Density must be positive.")

    return mass_kg / density