from enum import Enum

class PaymentFailureCode(Enum):
    PROVIDER_UNAVAILABLE = "provider_unavailable"
    PROVIDER_UNREACHABLE = "provider_unreachable"
    PROVIDER_NOT_CONFIGURED = "provider_not_configured"
    PROVIDER_DECLINED = "provider_declined"
    PROVIDER_ERROR = "provider_error"
