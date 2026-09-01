from enum import Enum

class CartStatus(Enum):
    ACTIVE = "active"
    ABANDONED = "abandoned"
    ORDERED = "ordered"
    MERGED = "merged"
