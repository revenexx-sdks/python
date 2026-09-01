from enum import Enum

class ShippingTaxUnresolvedReason(Enum):
    MARKET_REQUIRED = "market_required"
    NO_MARKETS = "no_markets"
    NO_TAX_CLASSES = "no_tax_classes"
    LOOKUP_FAILED = "lookup_failed"
