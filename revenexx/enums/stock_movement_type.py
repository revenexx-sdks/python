from enum import Enum

class StockMovementType(Enum):
    INBOUND = "inbound"
    ADJUSTMENT = "adjustment"
    RESERVE = "reserve"
    RELEASE = "release"
    SHIPMENT = "shipment"
    RESTOCK = "restock"
