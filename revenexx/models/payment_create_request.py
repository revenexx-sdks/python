from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class PaymentCreateRequest(AppwriteModel):
    """
    Creates AND authorizes: self-managed methods authorize immediately, PSP methods may answer next_action (redirect). Eligibility is re-checked server-side.

    Attributes
    ----------
    amount : float
        What the provider is asked to authorize, in `currency`. 0 is legal (a free order) and negative is refused by the handler and by the CHECK behind it. `fee_amount` is recorded beside this and is NOT added to it — a checkout that charges its payment surcharge sends a total that already includes it.
    cart_id : Optional[str]
        The cart this payment pays for. Not a foreign key: the payment is a record of what happened and outlives the cart. Indexed, so it is the cheap way to find the payment behind a checkout.
    contact_id : Optional[str]
        The paying customer contact. Not a foreign key — a payment must survive a contact being merged or erased. Indexed.
    country : Optional[str]
        The buyer&#039;s ISO 3166-1 alpha-2 country code, for the eligibility check. A method restricted to countries is refused with 422 without it.
    currency : Optional[str]
        ISO 4217 code the amount and the fee are in. The database bounds the length at three characters and nothing else, so lower case is stored as written. Defaults to EUR.
    idempotency_key : Optional[str]
        The caller&#039;s own key for this creation attempt. Sending it again answers the SAME payment with 200 instead of creating a second one — which is what makes a retried checkout safe. Unique per tenant, so a filter on it answers at most one row. The replay answers 200, not 201.
    metadata : Optional[Dict[str, Any]]
        Free-form data to keep on the payment. Merged with the keys this app writes itself (`provider_method`, `return_url`, later the cancel/refund reasons), which win on a collision.
    method_code : str
        The `code` of the payment method this payment was made with, copied at creation. Deliberately a code and not a foreign key: the ledger records what happened and has to outlive the configuration it happened under. It must name a method this tenant has configured; eligibility for the buyer context below is re-checked here, whatever the checkout showed.
    order_ref : Optional[str]
        The external order reference the checkout wrote onto the payment. It is what POST /payments/orders/{order_ref}/capture resolves and the fallback key a PSP webhook is matched on when it carries no transaction id — so an integration that leaves it null gives up both. Free text with no uniqueness: several payments may share one reference.
    return_url : Optional[str]
        Where the PSP sends the buyer back after a redirect or a 3-D Secure challenge. Kept in `metadata.return_url` and handed to the driver — a PSP method that needs a redirect and has none leaves the buyer stranded at the provider.
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
