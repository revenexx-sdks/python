from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class Cart(AppwriteModel):
    """
    

    Attributes
    ----------
    abandoned_at : Optional[str]
        Typed model field.
    channel_id : Optional[str]
        Typed model field.
    contact_id : Optional[str]
        Typed model field.
    created_at : Optional[str]
        Typed model field.
    currency : Optional[str]
        Typed model field.
    id : Optional[str]
        Typed model field.
    is_current : Optional[bool]
        Typed model field.
    item_count : Optional[float]
        Typed model field.
    market_id : Optional[str]
        Typed model field.
    merged_into_cart_id : Optional[str]
        Typed model field.
    metadata : Optional[Dict[str, Any]]
        Typed model field.
    name : Optional[str]
        Typed model field.
    order_ref : Optional[str]
        Typed model field.
    ordered_at : Optional[str]
        Typed model field.
    session_key : Optional[str]
        Typed model field.
    status : Optional[str]
        Typed model field.
    subtotal : Optional[float]
        Typed model field.
    updated_at : Optional[str]
        Typed model field.
    """
    abandoned_at: Optional[str] = Field(default=None, alias='abandoned_at')
    channel_id: Optional[str] = Field(default=None, alias='channel_id')
    contact_id: Optional[str] = Field(default=None, alias='contact_id')
    created_at: Optional[str] = Field(default=None, alias='created_at')
    currency: Optional[str] = Field(default=None, alias='currency')
    id: Optional[str] = Field(default=None, alias='id')
    is_current: Optional[bool] = Field(default=None, alias='is_current')
    item_count: Optional[float] = Field(default=None, alias='item_count')
    market_id: Optional[str] = Field(default=None, alias='market_id')
    merged_into_cart_id: Optional[str] = Field(default=None, alias='merged_into_cart_id')
    metadata: Optional[Dict[str, Any]] = Field(default=None, alias='metadata')
    name: Optional[str] = Field(default=None, alias='name')
    order_ref: Optional[str] = Field(default=None, alias='order_ref')
    ordered_at: Optional[str] = Field(default=None, alias='ordered_at')
    session_key: Optional[str] = Field(default=None, alias='session_key')
    status: Optional[str] = Field(default=None, alias='status')
    subtotal: Optional[float] = Field(default=None, alias='subtotal')
    updated_at: Optional[str] = Field(default=None, alias='updated_at')
