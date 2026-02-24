from quantifyx.exceptions import QuantifyXError


class InvalidMaterialError(QuantifyXError):
    """Raised when unsupported pipe material is requested."""
    pass


# Absolute roughness values in meters
_PIPE_ROUGHNESS = {
    "hdpe": 0.0000015,
    "pvc": 0.0000015,
    "di": 0.00026,
    "ci": 0.00026,
    "ms": 0.000045,
    "rcc": 0.0003,
}


def get_roughness(material: str) -> float:
    """
    Return pipe roughness (m) for given material.
    """
    material = material.lower()

    if material not in _PIPE_ROUGHNESS:
        raise InvalidMaterialError(f"Unsupported material: {material}")

    return _PIPE_ROUGHNESS[material]