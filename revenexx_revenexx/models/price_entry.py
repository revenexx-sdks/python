from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class PriceEntry(AppwriteModel):
    """
    

    Attributes
    ----------
    created_at : Optional[str]
        Typed model field.
    id : Optional[str]
        Typed model field.
    metadata : Optional[Dict[str, Any]]
        Typed model field.
    price_list_id : Optional[str]
        Typed model field.
    price_type : Optional[str]
        Typed model field.
    product_id : Optional[str]
        Typed model field.
    quantity_min : Optional[float]
        Typed model field.
    sku : Optional[str]
        Typed model field.
    unit : Optional[str]
        Typed model field.
    unit_price : Optional[float]
        Typed model field.
    updated_at : Optional[str]
        Typed model field.
    valid_from : Optional[str]
        Typed model field.
    valid_until : Optional[str]
        Typed model field.
    """
    created_at: Optional[str] = Field(default=None, alias='created_at')
    id: Optional[str] = Field(default=None, alias='id')
    metadata: Optional[Dict[str, Any]] = Field(default=None, alias='metadata')
    price_list_id: Optional[str] = Field(default=None, alias='price_list_id')
    price_type: Optional[str] = Field(default=None, alias='price_type')
    product_id: Optional[str] = Field(default=None, alias='product_id')
    quantity_min: Optional[float] = Field(default=None, alias='quantity_min')
    sku: Optional[str] = Field(default=None, alias='sku')
    unit: Optional[str] = Field(default=None, alias='unit')
    unit_price: Optional[float] = Field(default=None, alias='unit_price')
    updated_at: Optional[str] = Field(default=None, alias='updated_at')
    valid_from: Optional[str] = Field(default=None, alias='valid_from')
    valid_until: Optional[str] = Field(default=None, alias='valid_until')
