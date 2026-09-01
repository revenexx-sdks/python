from enum import Enum

class PaymentTermCreateRequestTone(Enum):
    NEUTRAL = "neutral"
    INFO = "info"
    SUCCESS = "success"
    WARNING = "warning"
    DANGER = "danger"
