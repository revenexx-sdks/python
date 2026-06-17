from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class Order(AppwriteModel):
    """
    

    Attributes
    ----------
    acknowledged_at : Optional[str]
        Typed model field.
    billing_address : Optional[Dict[str, Any]]
        Typed model field.
    buyer : Optional[Dict[str, Any]]
        Typed model field.
    cancelled_at : Optional[str]
        Typed model field.
    cart_id : Optional[str]
        Typed model field.
    channel_id : Optional[str]
        Typed model field.
    completed_at : Optional[str]
        Typed model field.
    contact_id : Optional[str]
        Typed model field.
    created_at : Optional[str]
        Typed model field.
    currency : Optional[str]
        Typed model field.
    customer_order_number : Optional[str]
        Typed model field.
    external_ref : Optional[str]
        Typed model field.
    fulfillment_status : Optional[str]
        Typed model field.
    grand_total : Optional[float]
        Typed model field.
    hold_reason : Optional[str]
        Typed model field.
    id : Optional[str]
        Typed model field.
    item_count : Optional[float]
        Typed model field.
    market_id : Optional[str]
        Typed model field.
    metadata : Optional[Dict[str, Any]]
        Typed model field.
    number : Optional[str]
        Typed model field.
    on_hold : Optional[bool]
        Typed model field.
    organization_id : Optional[str]
        Typed model field.
    payment : Optional[Dict[str, Any]]
        Typed model field.
    payment_status : Optional[str]
        Typed model field.
    placed_at : Optional[str]
        Typed model field.
    shipping : Optional[Dict[str, Any]]
        Typed model field.
    shipping_address : Optional[Dict[str, Any]]
        Typed model field.
    shipping_total : Optional[float]
        Typed model field.
    status : Optional[str]
        Typed model field.
    subtotal : Optional[float]
        Typed model field.
    tax_total : Optional[float]
        Typed model field.
    updated_at : Optional[str]
        Typed model field.
    user_data : Optional[Dict[str, Any]]
        Typed model field.
    """
    acknowledged_at: Optional[str] = Field(default=None, alias='acknowledged_at')
    billing_address: Optional[Dict[str, Any]] = Field(default=None, alias='billing_address')
    buyer: Optional[Dict[str, Any]] = Field(default=None, alias='buyer')
    cancelled_at: Optional[str] = Field(default=None, alias='cancelled_at')
    cart_id: Optional[str] = Field(default=None, alias='cart_id')
    channel_id: Optional[str] = Field(default=None, alias='channel_id')
    completed_at: Optional[str] = Field(default=None, alias='completed_at')
    contact_id: Optional[str] = Field(default=None, alias='contact_id')
    created_at: Optional[str] = Field(default=None, alias='created_at')
    currency: Optional[str] = Field(default=None, alias='currency')
    customer_order_number: Optional[str] = Field(default=None, alias='customer_order_number')
    external_ref: Optional[str] = Field(default=None, alias='external_ref')
    fulfillment_status: Optional[str] = Field(default=None, alias='fulfillment_status')
    grand_total: Optional[float] = Field(default=None, alias='grand_total')
    hold_reason: Optional[str] = Field(default=None, alias='hold_reason')
    id: Optional[str] = Field(default=None, alias='id')
    item_count: Optional[float] = Field(default=None, alias='item_count')
    market_id: Optional[str] = Field(default=None, alias='market_id')
    metadata: Optional[Dict[str, Any]] = Field(default=None, alias='metadata')
    number: Optional[str] = Field(default=None, alias='number')
    on_hold: Optional[bool] = Field(default=None, alias='on_hold')
    organization_id: Optional[str] = Field(default=None, alias='organization_id')
    payment: Optional[Dict[str, Any]] = Field(default=None, alias='payment')
    payment_status: Optional[str] = Field(default=None, alias='payment_status')
    placed_at: Optional[str] = Field(default=None, alias='placed_at')
    shipping: Optional[Dict[str, Any]] = Field(default=None, alias='shipping')
    shipping_address: Optional[Dict[str, Any]] = Field(default=None, alias='shipping_address')
    shipping_total: Optional[float] = Field(default=None, alias='shipping_total')
    status: Optional[str] = Field(default=None, alias='status')
    subtotal: Optional[float] = Field(default=None, alias='subtotal')
    tax_total: Optional[float] = Field(default=None, alias='tax_total')
    updated_at: Optional[str] = Field(default=None, alias='updated_at')
    user_data: Optional[Dict[str, Any]] = Field(default=None, alias='user_data')
