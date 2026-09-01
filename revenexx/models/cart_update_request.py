from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class CartUpdateRequest(AppwriteModel):
    """
    Only safe columns are updatable — status moves through the lifecycle routes.

    Attributes
    ----------
    channel_id : Optional[str]
        Move the cart to another sales channel.
    currency : Optional[str]
        ISO 4217 code. Changes what NEW lines inherit; lines already in the cart keep the currency they were added with.
    metadata : Optional[Dict[str, Any]]
        Free-form data the storefront hangs on the cart. Stored and returned verbatim; no key in here is read by this app, and none is indexed.
    name : Optional[str]
        Rename the cart. Unlike on create, this is written verbatim — `null` and `&#039;&#039;` are refused by the database.
    """
    channel_id: Optional[str] = Field(default=None, alias='channel_id')
    currency: Optional[str] = Field(default=None, alias='currency')
    metadata: Optional[Dict[str, Any]] = Field(default=None, alias='metadata')
    name: Optional[str] = Field(default=None, alias='name')
