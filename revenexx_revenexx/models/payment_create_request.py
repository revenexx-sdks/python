from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class PaymentCreateRequest(AppwriteModel):
    """
    Creates AND authorizes: self-managed methods authorize immediately, PSP methods may answer next_action (redirect). Eligibility is re-checked server-side.

    Attributes
    ----------
    amount : float
        Order amount — 0 is legal (free orders), negative is not.
    cart_id : Optional[str]
        The cart this payment pays for.
    contact_id : Optional[str]
        Paying customer contact.
    country : Optional[str]
        Buyer ISO country code for the eligibility check.
    currency : Optional[str]
        ISO 4217 code (default EUR).
    idempotency_key : Optional[str]
        Same key answers the same payment instead of a duplicate.
    metadata : Optional[Dict[str, Any]]
        Free-form metadata.
    method_code : str
        Code of a configured payment method.
    order_ref : Optional[str]
        External order reference — also the webhook fallback key.
    return_url : Optional[str]
        Where the PSP redirect flow returns the buyer to.
    """
    amount: float = Field(..., alias='amount')
    cart_id: Optional[str] = Field(default=None, alias='cart_id')
    contact_id: Optional[str] = Field(default=None, alias='contact_id')
    country: Optional[str] = Field(default=None, alias='country')
    currency: Optional[str] = Field(default=None, alias='currency')
    idempotency_key: Optional[str] = Field(default=None, alias='idempotency_key')
    metadata: Optional[Dict[str, Any]] = Field(default=None, alias='metadata')
    method_code: str = Field(..., alias='method_code')
    order_ref: Optional[str] = Field(default=None, alias='order_ref')
    return_url: Optional[str] = Field(default=None, alias='return_url')
