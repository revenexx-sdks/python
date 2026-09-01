from enum import Enum

class ProductLabelSource(Enum):
    COMMON = "common"
    LOCALE_SPECIFIC = "locale_specific"
    CHANNEL_SPECIFIC = "channel_specific"
    CHANNEL_LOCALE_SPECIFIC = "channel_locale_specific"
    SKU = "sku"
