from enum import Enum

class OrderReturnSettlement(Enum):
    REFUND = "refund"
    PARTIAL_REFUND = "partial_refund"
    REPLACEMENT = "replacement"
    REPAIR = "repair"
    STORE_CREDIT = "store_credit"
