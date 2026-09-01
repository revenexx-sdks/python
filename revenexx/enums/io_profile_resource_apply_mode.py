from enum import Enum

class IoProfileResourceApplyMode(Enum):
    UPSERT = "upsert"
    FULL_SYNC = "full-sync"
    APPEND = "append"
