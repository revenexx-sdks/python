from enum import Enum

class ShippingMethodPricingType(Enum):
    FIXED = "fixed"
    FREE = "free"
    MATRIX = "matrix"
