from enum import Enum

class MarketDefaultLocaleSource(Enum):
    MARKET = "market"
    MARKET_FIRST = "market_first"
    TENANT_FALLBACK = "tenant_fallback"
