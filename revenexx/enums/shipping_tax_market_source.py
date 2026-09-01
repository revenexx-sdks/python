from enum import Enum

class ShippingTaxMarketSource(Enum):
    REQUEST = "request"
    HEADER = "header"
    COUNTRY = "country"
    SOLE_MARKET = "sole_market"
