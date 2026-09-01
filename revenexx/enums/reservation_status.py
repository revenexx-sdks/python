from enum import Enum

class ReservationStatus(Enum):
    ACTIVE = "active"
    RELEASED = "released"
    COMMITTED = "committed"
