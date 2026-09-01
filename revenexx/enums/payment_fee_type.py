from enum import Enum

class PaymentFeeType(Enum):
    NONE = "none"
    FIXED = "fixed"
    PERCENT = "percent"
