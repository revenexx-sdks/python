from enum import Enum

class InventoriesReservationsListStatus(Enum):
    ACTIVE = "active"
    RELEASED = "released"
    COMMITTED = "committed"
