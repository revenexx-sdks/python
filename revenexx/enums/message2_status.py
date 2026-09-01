from enum import Enum

class Message2Status(Enum):
    DRAFT = "draft"
    PROCESSING = "processing"
    SCHEDULED = "scheduled"
    SENT = "sent"
    FAILED = "failed"
