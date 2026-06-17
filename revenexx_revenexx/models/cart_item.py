from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class CartItem(AppwriteModel):
    """
    

    Attributes
    ----------
    cart_id : Optional[str]
        Typed model field.
    configuration : Optional[Dict[str, Any]]
        Typed model field.
    created_at : Optional[str]
        Typed model field.
    currency : Optional[str]
        Typed model field.
    id : Optional[str]
        Typed model field.
    line_total : Optional[float]
        Typed model field.
    metadata : Optional[Dict[str, Any]]
        Typed model field.
    name : Optional[str]
        Typed model field.
    position : Optional[float]
        Typed model field.
    product_id : Optional[str]
        Typed model field.
    quantity : Optional[float]
        Typed model field.
    sku : Optional[str]
        Typed model field.
    snapshot : Optional[Dict[str, Any]]
        Typed model field.
    tax_rate : Optional[float]
        Typed model field.
    type : Optional[str]
        Typed model field.
    unit : Optional[str]
        Typed model field.
    unit_price : Optional[float]
        Typed model field.
    updated_at : Optional[str]
        Typed model field.
    """
    cart_id: Optional[str] = Field(default=None, alias='cart_id')
    configuration: Optional[Dict[str, Any]] = Field(default=None, alias='configuration')
    created_at: Optional[str] = Field(default=None, alias='created_at')
    currency: Optional[str] = Field(default=None, alias='currency')
    id: Optional[str] = Field(default=None, alias='id')
    line_total: Optional[float] = Field(default=None, alias='line_total')
    metadata: Optional[Dict[str, Any]] = Field(default=None, alias='metadata')
    name: Optional[str] = Field(default=None, alias='name')
    position: Optional[float] = Field(default=None, alias='position')
    product_id: Optional[str] = Field(default=None, alias='product_id')
    quantity: Optional[float] = Field(default=None, alias='quantity')
    sku: Optional[str] = Field(default=None, alias='sku')
    snapshot: Optional[Dict[str, Any]] = Field(default=None, alias='snapshot')
    tax_rate: Optional[float] = Field(default=None, alias='tax_rate')
    type: Optional[str] = Field(default=None, alias='type')
    unit: Optional[str] = Field(default=None, alias='unit')
    unit_price: Optional[float] = Field(default=None, alias='unit_price')
    updated_at: Optional[str] = Field(default=None, alias='updated_at')
