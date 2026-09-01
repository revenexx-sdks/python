from enum import Enum

class PaymentTermUpdateRequestTone(Enum):
    NEUTRAL = "neutral"
    INFO = "info"
    SUCCESS = "success"
    WARNING = "warning"
    DANGER = "danger"
