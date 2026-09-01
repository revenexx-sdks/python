from enum import Enum

class AttributeValueBucket(Enum):
    COMMON = "common"
    LOCALE_SPECIFIC = "locale_specific"
    CHANNEL_SPECIFIC = "channel_specific"
    CHANNEL_LOCALE_SPECIFIC = "channel_locale_specific"
