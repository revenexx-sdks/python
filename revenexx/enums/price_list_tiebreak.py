from enum import Enum

class PriceListTiebreak(Enum):
    LOWEST_PRICE = "lowest_price"
    HIGHEST_PRICE = "highest_price"
    NEWEST = "newest"
    CODE = "code"
