from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class OrderItem(AppwriteModel):
    """
    

    Attributes
    ----------
    configuration : Optional[Dict[str, Any]]
        Typed model field.
    cost_center : Optional[str]
        Typed model field.
    created_at : Optional[str]
        Typed model field.
    id : Optional[str]
        Typed model field.
    line_total : Optional[float]
        Typed model field.
    metadata : Optional[Dict[str, Any]]
        Typed model field.
    name : Optional[str]
        Typed model field.
    order_id : Optional[str]
        Typed model field.
    position : Optional[float]
        Typed model field.
    position_text : Optional[str]
        Typed model field.
    product : Optional[Dict[str, Any]]
        Typed model field.
    product_id : Optional[str]
        Typed model field.
    quantity : Optional[float]
        Typed model field.
    quantity_cancelled : Optional[float]
        Typed model field.
    quantity_returned : Optional[float]
        Typed model field.
    quantity_shipped : Optional[float]
        Typed model field.
    sku : Optional[str]
        Typed model field.
    tax_amount : Optional[float]
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
    user_data : Optional[Dict[str, Any]]
        Typed model field.
    """
    configuration: Optional[Dict[str, Any]] = Field(default=None, alias='configuration')
    cost_center: Optional[str] = Field(default=None, alias='cost_center')
    created_at: Optional[str] = Field(default=None, alias='created_at')
    id: Optional[str] = Field(default=None, alias='id')
    line_total: Optional[float] = Field(default=None, alias='line_total')
    metadata: Optional[Dict[str, Any]] = Field(default=None, alias='metadata')
    name: Optional[str] = Field(default=None, alias='name')
    order_id: Optional[str] = Field(default=None, alias='order_id')
    position: Optional[float] = Field(default=None, alias='position')
    position_text: Optional[str] = Field(default=None, alias='position_text')
    product: Optional[Dict[str, Any]] = Field(default=None, alias='product')
    product_id: Optional[str] = Field(default=None, alias='product_id')
    quantity: Optional[float] = Field(default=None, alias='quantity')
    quantity_cancelled: Optional[float] = Field(default=None, alias='quantity_cancelled')
    quantity_returned: Optional[float] = Field(default=None, alias='quantity_returned')
    quantity_shipped: Optional[float] = Field(default=None, alias='quantity_shipped')
    sku: Optional[str] = Field(default=None, alias='sku')
    tax_amount: Optional[float] = Field(default=None, alias='tax_amount')
    tax_rate: Optional[float] = Field(default=None, alias='tax_rate')
    type: Optional[str] = Field(default=None, alias='type')
    unit: Optional[str] = Field(default=None, alias='unit')
    unit_price: Optional[float] = Field(default=None, alias='unit_price')
    updated_at: Optional[str] = Field(default=None, alias='updated_at')
    user_data: Optional[Dict[str, Any]] = Field(default=None, alias='user_data')
