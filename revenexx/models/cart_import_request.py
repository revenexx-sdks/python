from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class CartImportRequest(AppwriteModel):
    """
    Import into an existing cart (&#039;target_cart_id&#039;) or a new cart (owner &#039;contact_id&#039;/&#039;session_key&#039; required).

    Attributes
    ----------
    contact_id : Optional[str]
        Owner of the cart this import creates. Ignored when target_cart_id is sent.
    csv : Optional[str]
        The CSV rows, when that is easier than putting them in `payload`. First line is the header, and its names are the ones the profile&#039;s mapping expects (the bundled quick-order template reads sku, name, quantity, unit_price). Numbers are coerced; a JSON column survives as a JSON string.
    name : Optional[str]
        Name for the cart this import creates. A name in the payload&#039;s own `cart` block wins over it; without either the cart is called &#039;Imported cart&#039;.
    payload : Optional[Dict[str, Any]]
        The import itself. As an object: `{ &quot;cart&quot;: { name, status, currency, channel_id, metadata }, &quot;items&quot;: [ … ] }` — the same document carts.export produces, so an export round-trips. As a string: that document as raw JSON, or CSV rows when the profile is a csv one. A line with neither `name` nor `sku` is dropped, and a payload that leaves no line at all is a 400.
    profile_id : Optional[str]
        The import profile to run — one of the ids `GET /carts/io/profiles?direction=import` lists. Omit it for an ad-hoc import: the payload is then read in the canonical shape, and as CSV if `csv` is what carried it.
    session_key : Optional[str]
        Guest owner of the cart this import creates — the storefront&#039;s own session key. Ignored when target_cart_id is sent.
    target_cart_id : Optional[str]
        An existing ACTIVE cart to import into. The lines are added to it (merging identical product lines), unless the profile says `apply_mode: replace`, which clears it first. Without this a new cart is created and an owner is required.
    """
    contact_id: Optional[str] = Field(default=None, alias='contact_id')
    csv: Optional[str] = Field(default=None, alias='csv')
    name: Optional[str] = Field(default=None, alias='name')
    payload: Optional[Dict[str, Any]] = Field(default=None, alias='payload')
    profile_id: Optional[str] = Field(default=None, alias='profile_id')
    session_key: Optional[str] = Field(default=None, alias='session_key')
    target_cart_id: Optional[str] = Field(default=None, alias='target_cart_id')
