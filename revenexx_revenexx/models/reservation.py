from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class Reservation(AppwriteModel):
    """
    

    Attributes
    ----------
    created_at : Optional[str]
        Typed model field.
    expires_at : Optional[str]
        Typed model field.
    id : Optional[str]
        Typed model field.
    location_id : Optional[str]
        Typed model field.
    metadata : Optional[Dict[str, Any]]
        Typed model field.
    order_ref : Optional[str]
        Typed model field.
    product_id : Optional[str]
        Typed model field.
    quantity : Optional[float]
        Typed model field.
    sku : Optional[str]
        Typed model field.
    status : Optional[str]
        Typed model field.
    updated_at : Optional[str]
        Typed model field.
    """
    created_at: Optional[str] = Field(default=None, alias='created_at')
    expires_at: Optional[str] = Field(default=None, alias='expires_at')
    id: Optional[str] = Field(default=None, alias='id')
    location_id: Optional[str] = Field(default=None, alias='location_id')
    metadata: Optional[Dict[str, Any]] = Field(default=None, alias='metadata')
    order_ref: Optional[str] = Field(default=None, alias='order_ref')
    product_id: Optional[str] = Field(default=None, alias='product_id')
    quantity: Optional[float] = Field(default=None, alias='quantity')
    sku: Optional[str] = Field(default=None, alias='sku')
    status: Optional[str] = Field(default=None, alias='status')
    updated_at: Optional[str] = Field(default=None, alias='updated_at')
