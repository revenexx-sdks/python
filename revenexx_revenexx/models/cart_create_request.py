from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class CartCreateRequest(AppwriteModel):
    """
    A cart needs an owner: &#039;contact_id&#039; (customer) or &#039;session_key&#039; (guest).

    Attributes
    ----------
    channel_id : Optional[str]
        Typed model field.
    contact_id : Optional[str]
        Owning customer contact.
    currency : Optional[str]
        ISO 4217 code (default EUR).
    is_current : Optional[bool]
        Make this THE current cart of its owner.
    market_id : Optional[str]
        Typed model field.
    metadata : Optional[Dict[str, Any]]
        Free-form metadata.
    name : Optional[str]
        Display name (default &#039;Cart&#039;).
    session_key : Optional[str]
        Owning guest session.
    """
    channel_id: Optional[str] = Field(default=None, alias='channel_id')
    contact_id: Optional[str] = Field(default=None, alias='contact_id')
    currency: Optional[str] = Field(default=None, alias='currency')
    is_current: Optional[bool] = Field(default=None, alias='is_current')
    market_id: Optional[str] = Field(default=None, alias='market_id')
    metadata: Optional[Dict[str, Any]] = Field(default=None, alias='metadata')
    name: Optional[str] = Field(default=None, alias='name')
    session_key: Optional[str] = Field(default=None, alias='session_key')
