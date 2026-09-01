from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class PaymentEligibilityRequest(AppwriteModel):
    """
    The buyer context — restriction dimensions are ANDed, entries within a dimension ORed, empty = unrestricted.

    Attributes
    ----------
    amount : Optional[float]
        The order amount the order-value bounds are checked against and the percentage fees are computed from. Defaults to 0, which excludes every method carrying a minimum. Nothing is written, so the ledger&#039;s own amount bound does not apply here.
    country : Optional[str]
        The buyer&#039;s ISO 3166-1 alpha-2 country code. A method restricted to countries is excluded without it — an unknown buyer sees only the unrestricted methods, which is the safe default and not a bug.
    currency : Optional[str]
        ISO 4217 code the amount is in, echoed onto every computed fee. Defaults to EUR. This app does no conversion: the fee comes back in the currency it was asked with.
    """
    amount: Optional[float] = Field(default=None, alias='amount')
    country: Optional[str] = Field(default=None, alias='country')
    currency: Optional[str] = Field(default=None, alias='currency')
