from enum import Enum

class PaymentStatus(Enum):
    CREATED = "created"
    REQUIRES_ACTION = "requires_action"
    AUTHORIZED = "authorized"
    CAPTURED = "captured"
    FAILED = "failed"
    CANCELLED = "cancelled"
    REFUNDED = "refunded"
