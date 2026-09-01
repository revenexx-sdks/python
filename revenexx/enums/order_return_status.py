from enum import Enum

class OrderReturnStatus(Enum):
    REGISTERED = "registered"
    RECEIVED = "received"
    COMPLETED = "completed"
    REJECTED = "rejected"
