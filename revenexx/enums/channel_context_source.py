from enum import Enum

class ChannelContextSource(Enum):
    BODY = "body"
    QUERY = "query"
    HEADER = "header"
    JWT = "jwt"
    DEFAULT = "default"
