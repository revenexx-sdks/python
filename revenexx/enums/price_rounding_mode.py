from enum import Enum

class PriceRoundingMode(Enum):
    HALF_UP = "half_up"
    HALF_EVEN = "half_even"
    UP = "up"
    DOWN = "down"
