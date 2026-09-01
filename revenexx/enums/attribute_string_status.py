from enum import Enum

class AttributeStringStatus(Enum):
    AVAILABLE = "available"
    PROCESSING = "processing"
    DELETING = "deleting"
    STUCK = "stuck"
    FAILED = "failed"
