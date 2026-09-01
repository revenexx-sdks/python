from enum import Enum

class VocabularySource(Enum):
    SCHEMA = "schema"
    TABLE = "table"
    TENANT = "tenant"
    DEFAULTS = "defaults"
