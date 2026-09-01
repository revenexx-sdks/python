from enum import Enum

class PriceTaxBasisSource(Enum):
    LIST = "list"
    LIST_LEGACY = "list_legacy"
    TENANT = "tenant"
