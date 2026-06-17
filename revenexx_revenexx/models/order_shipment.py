from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class OrderShipment(AppwriteModel):
    """
    

    Attributes
    ----------
    carrier : Optional[str]
        Typed model field.
    created_at : Optional[str]
        Typed model field.
    id : Optional[str]
        Typed model field.
    metadata : Optional[Dict[str, Any]]
        Typed model field.
    number : Optional[str]
        Typed model field.
    order_id : Optional[str]
        Typed model field.
    shipped_at : Optional[str]
        Typed model field.
    tracking_code : Optional[str]
        Typed model field.
    tracking_url : Optional[str]
        Typed model field.
    """
    carrier: Optional[str] = Field(default=None, alias='carrier')
    created_at: Optional[str] = Field(default=None, alias='created_at')
    id: Optional[str] = Field(default=None, alias='id')
    metadata: Optional[Dict[str, Any]] = Field(default=None, alias='metadata')
    number: Optional[str] = Field(default=None, alias='number')
    order_id: Optional[str] = Field(default=None, alias='order_id')
    shipped_at: Optional[str] = Field(default=None, alias='shipped_at')
    tracking_code: Optional[str] = Field(default=None, alias='tracking_code')
    tracking_url: Optional[str] = Field(default=None, alias='tracking_url')
