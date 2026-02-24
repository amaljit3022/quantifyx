from quantifyx.exceptions import QuantifyXError


class InvalidDarcyInputError(QuantifyXError):
    """Raised when invalid inputs are given to Darcy-Weisbach calculations."""
    pass


_GRAVITY = 9.80665


def reynolds_number(velocity_ms: float, diameter_m: float, kinematic_viscosity: float) -> float:
    """
    Calculate Reynolds number.
    """
    if velocity_ms <= 0 or diameter_m <= 0 or kinematic_viscosity <= 0:
        raise InvalidDarcyInputError("All inputs must be positive.")

    return (velocity_ms * diameter_m) / kinematic_viscosity


def friction_factor_laminar(reynolds: float) -> float:
    """
    Friction factor for laminar flow (Re < 2000).
    """
    if reynolds <= 0:
        raise InvalidDarcyInputError("Reynolds number must be positive.")

    return 64 / reynolds


def friction_factor_blasius(reynolds: float) -> float:
    """
    Blasius approximation (valid roughly for 4000 < Re < 100000).
    """
    if reynolds <= 0:
        raise InvalidDarcyInputError("Reynolds number must be positive.")

    return 0.3164 / (reynolds ** 0.25)


def headloss_darcy(
    friction_factor: float,
    length_m: float,
    diameter_m: float,
    velocity_ms: float,
) -> float:
    """
    Calculate headloss using Darcy-Weisbach equation.
    """
    if friction_factor <= 0 or length_m <= 0 or diameter_m <= 0 or velocity_ms <= 0:
        raise InvalidDarcyInputError("All inputs must be positive.")

    return (
        friction_factor
        * (length_m / diameter_m)
        * (velocity_ms ** 2 / (2 * _GRAVITY))
    )