from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class PaymentTransitionRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    reason : Optional[str]
        The operator&#039;s own words for why. Kept on the payment (`metadata.cancel_reason` / `metadata.refund_reason`) AND handed to the provider&#039;s own cancellation or refund reason field, so it is readable in the PSP&#039;s dashboard too. Trimmed and cut at 500 characters.
    """
    reason: Optional[str] = Field(default=None, alias='reason')
