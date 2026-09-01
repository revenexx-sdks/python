from enum import Enum

class ShippingTaxSource(Enum):
    METHOD = "method"
    TENANT_CLASS = "tenant_class"
    MARKET_DEFAULT = "market_default"
    TENANT_DEFAULT = "tenant_default"
