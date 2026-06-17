from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class CartUpdateRequest(AppwriteModel):
    """
    Only safe columns are updatable — status moves through the lifecycle routes.

    Attributes
    ----------
    channel_id : Optional[str]
        Typed model field.
    currency : Optional[str]
        ISO 4217 code.
    market_id : Optional[str]
        Typed model field.
    metadata : Optional[Dict[str, Any]]
        Free-form metadata.
    name : Optional[str]
        Typed model field.
    """
    channel_id: Optional[str] = Field(default=None, alias='channel_id')
    currency: Optional[str] = Field(default=None, alias='currency')
    market_id: Optional[str] = Field(default=None, alias='market_id')
    metadata: Optional[Dict[str, Any]] = Field(default=None, alias='metadata')
    name: Optional[str] = Field(default=None, alias='name')
