from enum import Enum

class MarketReadinessWarnings(Enum):
    LOCALES = "locales"
    CURRENCIES = "currencies"
    TAX_CLASSES = "tax_classes"
    TAX_BASIS = "tax_basis"
