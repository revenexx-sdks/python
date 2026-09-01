from enum import Enum

class PriceTaxMarketSource(Enum):
    REQUEST = "request"
    HEADER = "header"
    SOLE_MARKET = "sole_market"
