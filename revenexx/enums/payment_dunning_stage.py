from enum import Enum

class PaymentDunningStage(Enum):
    NONE = "none"
    REMINDER = "reminder"
    OVERDUE = "overdue"
