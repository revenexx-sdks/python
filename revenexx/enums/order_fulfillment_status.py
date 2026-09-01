from enum import Enum

class OrderFulfillmentStatus(Enum):
    UNFULFILLED = "unfulfilled"
    PARTIAL = "partial"
    FULFILLED = "fulfilled"
