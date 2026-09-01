from enum import Enum

class Mode(Enum):
    UPSERT = "upsert"
    FULL_SYNC = "full-sync"
    APPEND = "append"
