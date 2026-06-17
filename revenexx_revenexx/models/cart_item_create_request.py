from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.cart_item_type import CartItemType

class CartItemCreateRequest(AppwriteModel):
    """
    An item needs an identity: &#039;name&#039; or &#039;sku&#039;.

    Attributes
    ----------
    configuration : Optional[Dict[str, Any]]
        Free-form configuration — configured lines never merge.
    currency : Optional[str]
        Defaults to the cart&#039;s currency.
    metadata : Optional[Dict[str, Any]]
        Free-form metadata.
    name : Optional[str]
        Falls back to &#039;sku&#039; when omitted.
    position : Optional[float]
        Typed model field.
    product_id : Optional[str]
        Typed model field.
    quantity : Optional[float]
        Default 1.
    sku : Optional[str]
        Typed model field.
    snapshot : Optional[Dict[str, Any]]
        Loose product snapshot at add-time (price, name, image, …).
    tax_rate : Optional[float]
        Typed model field.
    type : Optional[CartItemType]
        Line type (default &#039;product&#039;). Plain product lines merge by product+price; configurations always stand alone.
    unit : Optional[str]
        Typed model field.
    unit_price : Optional[float]
        Per-unit net price — line_total is always derived.
    """
    configuration: Optional[Dict[str, Any]] = Field(default=None, alias='configuration')
    currency: Optional[str] = Field(default=None, alias='currency')
    metadata: Optional[Dict[str, Any]] = Field(default=None, alias='metadata')
    name: Optional[str] = Field(default=None, alias='name')
    position: Optional[float] = Field(default=None, alias='position')
    product_id: Optional[str] = Field(default=None, alias='product_id')
    quantity: Optional[float] = Field(default=None, alias='quantity')
    sku: Optional[str] = Field(default=None, alias='sku')
    snapshot: Optional[Dict[str, Any]] = Field(default=None, alias='snapshot')
    tax_rate: Optional[float] = Field(default=None, alias='tax_rate')
    type: Optional[CartItemType] = Field(default=None, alias='type')
    unit: Optional[str] = Field(default=None, alias='unit')
    unit_price: Optional[float] = Field(default=None, alias='unit_price')
