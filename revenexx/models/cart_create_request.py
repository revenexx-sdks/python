from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class CartCreateRequest(AppwriteModel):
    """
    A cart needs an owner: &#039;contact_id&#039; (customer) or &#039;session_key&#039; (guest).

    Attributes
    ----------
    channel_id : Optional[str]
        The sales channel this cart is being opened in, as a channel of the channels app. Stored for attribution; nothing in this app reads it.
    contact_id : Optional[str]
        The customer who owns this cart, as a contact of the customers app. Send this OR session_key — a cart with neither owner is refused.
    currency : Optional[str]
        ISO 4217 code the cart is priced in (default EUR). Lines added without a currency inherit it.
    is_current : Optional[bool]
        Make this THE current cart of its owner as it is created — the same thing carts.activate does later, and it clears the flag on every sibling cart of the same owner.
    metadata : Optional[Dict[str, Any]]
        Free-form data the storefront hangs on the cart. Stored and returned verbatim; no key in here is read by this app, and none is indexed.
    name : Optional[str]
        What the buyer calls this cart (default &#039;Cart&#039;). An empty string is legal and lands on the default.
    session_key : Optional[str]
        The guest session that owns this cart — the key the storefront already keeps in its own session or cookie. Any non-empty string is accepted; this app issues none and parses none, so the example shows a shape and not a format. Send this OR contact_id.
    """
    channel_id: Optional[str] = Field(default=None, alias='channel_id')
    contact_id: Optional[str] = Field(default=None, alias='contact_id')
    currency: Optional[str] = Field(default=None, alias='currency')
    is_current: Optional[bool] = Field(default=None, alias='is_current')
    metadata: Optional[Dict[str, Any]] = Field(default=None, alias='metadata')
    name: Optional[str] = Field(default=None, alias='name')
    session_key: Optional[str] = Field(default=None, alias='session_key')
