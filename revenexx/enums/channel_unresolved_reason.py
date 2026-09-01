from enum import Enum

class ChannelUnresolvedReason(Enum):
    CHANNEL_REQUIRED = "channel_required"
    NO_DEFAULT_CHANNEL = "no_default_channel"
    UNKNOWN_CHANNEL = "unknown_channel"
    CHANNEL_INACTIVE = "channel_inactive"
