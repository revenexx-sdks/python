from enum import Enum

class ChannelVisibilityReason(Enum):
    ASSIGNED = "assigned"
    NOT_ASSIGNED_TO_CHANNEL = "not_assigned_to_channel"
    UNASSIGNED_OPEN = "unassigned_open"
    UNASSIGNED_CLOSED = "unassigned_closed"
    NO_CHANNEL_CONTEXT = "no_channel_context"
