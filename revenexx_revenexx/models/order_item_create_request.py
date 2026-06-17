from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.order_item_type import OrderItemType

class OrderItemCreateRequest(AppwriteModel):
    """
    A position of the placed order — needs an identity: &#039;name&#039; or &#039;sku&#039;. Items are SNAPSHOTS: carry the product copy, prices are frozen at place-time.

    Attributes
    ----------
    configuration : Optional[Dict[str, Any]]
        Free-form configuration of configured lines.
    cost_center : Optional[str]
        Typed model field.
    metadata : Optional[Dict[str, Any]]
        Free-form metadata.
    name : Optional[str]
        Falls back to &#039;sku&#039; when omitted.
    position : Optional[float]
        Explicit position number; otherwise numbered in steps of the order range&#039;s position_step.
    position_text : Optional[str]
        Typed model field.
    product : Optional[Dict[str, Any]]
        Frozen product snapshot at place-time (&#039;snapshot&#039; is accepted as an alias).
    product_id : Optional[str]
        Typed model field.
    quantity : Optional[float]
        Default 1.
    sku : Optional[str]
        Typed model field.
    snapshot : Optional[Dict[str, Any]]
        Alias for &#039;product&#039;.
    tax_amount : Optional[float]
        Derived from line_total and tax_rate when omitted.
    tax_rate : Optional[float]
        Percent (default 0).
    type : Optional[OrderItemType]
        Line type (default &#039;product&#039;).
    unit : Optional[str]
        Typed model field.
    unit_price : Optional[float]
        Per-unit net price — line_total is always derived.
    user_data : Optional[Dict[str, Any]]
        Free-form user data.
    """
    configuration: Optional[Dict[str, Any]] = Field(default=None, alias='configuration')
    cost_center: Optional[str] = Field(default=None, alias='cost_center')
    metadata: Optional[Dict[str, Any]] = Field(default=None, alias='metadata')
    name: Optional[str] = Field(default=None, alias='name')
    position: Optional[float] = Field(default=None, alias='position')
    position_text: Optional[str] = Field(default=None, alias='position_text')
    product: Optional[Dict[str, Any]] = Field(default=None, alias='product')
    product_id: Optional[str] = Field(default=None, alias='product_id')
    quantity: Optional[float] = Field(default=None, alias='quantity')
    sku: Optional[str] = Field(default=None, alias='sku')
    snapshot: Optional[Dict[str, Any]] = Field(default=None, alias='snapshot')
    tax_amount: Optional[float] = Field(default=None, alias='tax_amount')
    tax_rate: Optional[float] = Field(default=None, alias='tax_rate')
    type: Optional[OrderItemType] = Field(default=None, alias='type')
    unit: Optional[str] = Field(default=None, alias='unit')
    unit_price: Optional[float] = Field(default=None, alias='unit_price')
    user_data: Optional[Dict[str, Any]] = Field(default=None, alias='user_data')
