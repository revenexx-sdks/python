from enum import Enum

class InventoriesMovementsListType(Enum):
    INBOUND = "inbound"
    ADJUSTMENT = "adjustment"
    RESERVE = "reserve"
    RELEASE = "release"
    SHIPMENT = "shipment"
    RESTOCK = "restock"
