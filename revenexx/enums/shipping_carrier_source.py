from enum import Enum

class ShippingCarrierSource(Enum):
    METHOD = "method"
    METHOD_CODE = "method_code"
    METHOD_TEXT = "method_text"
    TENANT_DEFAULT = "tenant_default"
    TENANT_DEFAULT_TEXT = "tenant_default_text"
