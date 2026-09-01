from enum import Enum

class PriceOnRequestReason(Enum):
    NOT_PRICED = "not_priced"
    ON_REQUEST_ENTRY = "on_request_entry"
    ANONYMOUS_DENIED = "anonymous_denied"
    NO_IDENTITY = "no_identity"
