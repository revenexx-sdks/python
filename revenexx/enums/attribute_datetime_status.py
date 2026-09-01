from enum import Enum

class AttributeDatetimeStatus(Enum):
    AVAILABLE = "available"
    PROCESSING = "processing"
    DELETING = "deleting"
    STUCK = "stuck"
    FAILED = "failed"
