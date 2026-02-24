class QuantifyXError(Exception):
    """
    Base exception class for all QuantifyX-specific errors.
    """
    pass


class InvalidDimensionError(QuantifyXError):
    """
    Raised when a geometric dimension is invalid.
    """
    pass