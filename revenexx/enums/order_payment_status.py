from enum import Enum

class OrderPaymentStatus(Enum):
    OPEN = "open"
    PENDING = "pending"
    AUTHORIZED = "authorized"
    PAID = "paid"
    PARTIALLY_PAID = "partially_paid"
    REFUNDED = "refunded"
    FAILED = "failed"
