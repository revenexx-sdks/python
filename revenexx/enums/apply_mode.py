from enum import Enum

class ApplyMode(Enum):
    UPSERT = "upsert"
    FULL_SYNC = "full-sync"
    APPEND = "append"
