from enum import Enum

class PageEditStateStatus(Enum):
    ACTIVE = "active"
    SCHEDULED = "scheduled"
    ARCHIVED = "archived"
    PUBLISHED = "published"
