import math
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

def friction_factor_colebrook(
    reynolds: float,
    diameter_m: float,
    roughness_m: float,
    tol: float = 1e-6,
    max_iter: int = 100,
) -> float:
    """
    Solve Colebrook-White equation for friction factor using iteration.

    Parameters
    ----------
    reynolds : float
        Reynolds number
    diameter_m : float
        Pipe diameter (m)
    roughness_m : float
        Absolute roughness (m)

    Returns
    -------
    float
        Darcy friction factor
    """
    if reynolds <= 0 or diameter_m <= 0 or roughness_m < 0:
        raise InvalidDarcyInputError("Invalid inputs for Colebrook equation.")

    # Initial guess (Blasius as starting point)
    f = 0.02

    for _ in range(max_iter):
        lhs = 1 / math.sqrt(f)
        rhs = -2.0 * math.log10(
            (roughness_m / (3.7 * diameter_m))
            + (2.51 / (reynolds * math.sqrt(f)))
        )

        new_f = 1 / (rhs ** 2)

        if abs(new_f - f) < tol:
            return new_f

        f = new_f

    raise InvalidDarcyInputError("Colebrook equation did not converge.")

def friction_factor_auto(
    reynolds: float,
    diameter_m: float,
    roughness_m: float = 0.0,
) -> float:
    """
    Automatically select appropriate friction factor model.

    Parameters
    ----------
    reynolds : float
    diameter_m : float
    roughness_m : float (default 0 for smooth pipe)

    Returns
    -------
    float
        Darcy friction factor
    """
    if reynolds <= 0 or diameter_m <= 0 or roughness_m < 0:
        raise InvalidDarcyInputError("Invalid inputs for friction factor.")

    # Laminar flow
    if reynolds < 2000:
        return friction_factor_laminar(reynolds)

    # Turbulent smooth pipe
    if roughness_m == 0:
        return friction_factor_blasius(reynolds)

    # Turbulent rough pipe
    return friction_factor_colebrook(reynolds, diameter_m, roughness_m)