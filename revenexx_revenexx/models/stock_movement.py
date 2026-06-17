from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class StockMovement(AppwriteModel):
    """
    

    Attributes
    ----------
    created_at : Optional[str]
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
    reason : Optional[str]
        Typed model field.
    sku : Optional[str]
        Typed model field.
    type : Optional[str]
        Typed model field.
    """
    created_at: Optional[str] = Field(default=None, alias='created_at')
    id: Optional[str] = Field(default=None, alias='id')
    location_id: Optional[str] = Field(default=None, alias='location_id')
    metadata: Optional[Dict[str, Any]] = Field(default=None, alias='metadata')
    order_ref: Optional[str] = Field(default=None, alias='order_ref')
    product_id: Optional[str] = Field(default=None, alias='product_id')
    quantity: Optional[float] = Field(default=None, alias='quantity')
    reason: Optional[str] = Field(default=None, alias='reason')
    sku: Optional[str] = Field(default=None, alias='sku')
    type: Optional[str] = Field(default=None, alias='type')
