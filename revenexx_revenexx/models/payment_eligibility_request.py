from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class PaymentEligibilityRequest(AppwriteModel):
    """
    The buyer context — restriction dimensions are ANDed, entries within a dimension ORed, empty = unrestricted.

    Attributes
    ----------
    amount : Optional[float]
        Order amount the fees are computed against (default 0).
    country : Optional[str]
        Buyer ISO country code — methods with country restrictions need it.
    currency : Optional[str]
        ISO 4217 code (default EUR).
    """
    amount: Optional[float] = Field(default=None, alias='amount')
    country: Optional[str] = Field(default=None, alias='country')
    currency: Optional[str] = Field(default=None, alias='currency')
