from enum import Enum

class FormSubmissionStatus(Enum):
    NEW = "new"
    READ = "read"
    ARCHIVED = "archived"
    SPAM = "spam"
