from enum import Enum

class PriceEntriesBulkMode(Enum):
    UPSERT = "upsert"
    APPEND = "append"
