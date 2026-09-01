from enum import Enum

class PriceCurrencySource(Enum):
    REQUEST = "request"
    MARKET = "market"
    TENANT = "tenant"
    FALLBACK = "fallback"
