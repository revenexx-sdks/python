from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class StockLevel(AppwriteModel):
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
    on_hand : Optional[float]
        Typed model field.
    product_id : Optional[str]
        Typed model field.
    reorder_point : Optional[float]
        Typed model field.
    reserved : Optional[float]
        Typed model field.
    sku : Optional[str]
        Typed model field.
    updated_at : Optional[str]
        Typed model field.
    """
    created_at: Optional[str] = Field(default=None, alias='created_at')
    id: Optional[str] = Field(default=None, alias='id')
    location_id: Optional[str] = Field(default=None, alias='location_id')
    metadata: Optional[Dict[str, Any]] = Field(default=None, alias='metadata')
    on_hand: Optional[float] = Field(default=None, alias='on_hand')
    product_id: Optional[str] = Field(default=None, alias='product_id')
    reorder_point: Optional[float] = Field(default=None, alias='reorder_point')
    reserved: Optional[float] = Field(default=None, alias='reserved')
    sku: Optional[str] = Field(default=None, alias='sku')
    updated_at: Optional[str] = Field(default=None, alias='updated_at')
