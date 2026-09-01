from enum import Enum

class ColumnDatetimeStatus(Enum):
    AVAILABLE = "available"
    PROCESSING = "processing"
    DELETING = "deleting"
    STUCK = "stuck"
    FAILED = "failed"
