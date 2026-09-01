from enum import Enum

class FormSubmissionPruneRequestStatus(Enum):
    NEW = "new"
    READ = "read"
    ARCHIVED = "archived"
    SPAM = "spam"
