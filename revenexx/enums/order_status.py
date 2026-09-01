from enum import Enum

class OrderStatus(Enum):
    PENDING = "pending"
    PLACED = "placed"
    IN_FULFILLMENT = "in_fulfillment"
    COMPLETED = "completed"
    CANCELLED = "cancelled"
