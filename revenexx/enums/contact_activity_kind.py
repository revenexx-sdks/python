from enum import Enum

class ContactActivityKind(Enum):
    NOTE = "note"
    CALL = "call"
    EMAIL = "email"
    MEETING = "meeting"
    VISIT = "visit"
    TASK = "task"
