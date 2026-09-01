from enum import Enum

class Reason(Enum):
    HARD_BOUNCE = "hard_bounce"
    COMPLAINT = "complaint"
    UNSUBSCRIBE = "unsubscribe"
    MANUAL = "manual"
