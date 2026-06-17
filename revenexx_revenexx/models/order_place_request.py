from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .order_item_create_request import OrderItemCreateRequest

class OrderPlaceRequest(AppwriteModel):
    """
    The snapshot payload: items plus frozen buyer/addresses/payment/shipping. The order number is drawn from the order range, totals are computed from the items.

    Attributes
    ----------
    billing_address : Optional[Dict[str, Any]]
        Frozen billing address.
    buyer : Optional[Dict[str, Any]]
        Frozen buyer snapshot (name, email, …).
    cart_id : Optional[str]
        Source cart (the carts.order hand-over).
    channel_id : Optional[str]
        Typed model field.
    contact_id : Optional[str]
        Ordering customer contact.
    currency : Optional[str]
        ISO 4217 code (default EUR).
    customer_order_number : Optional[str]
        The buyer&#039;s own order/PO number.
    grand_total : Optional[float]
        Override — computed as subtotal + shipping + tax when omitted.
    items : List[OrderItemCreateRequest]
        The order positions (at most 500).
    market_id : Optional[str]
        Typed model field.
    metadata : Optional[Dict[str, Any]]
        Free-form metadata.
    organization_id : Optional[str]
        B2B organization.
    payment : Optional[Dict[str, Any]]
        Frozen payment snapshot — a known &#039;payment.status&#039; seeds payment_status (otherwise &#039;open&#039;).
    shipping : Optional[Dict[str, Any]]
        Frozen shipping snapshot — &#039;shipping.price&#039; seeds shipping_total.
    shipping_address : Optional[Dict[str, Any]]
        Frozen shipping address.
    shipping_total : Optional[float]
        Shipping total (fallback when &#039;shipping.price&#039; is absent).
    user_data : Optional[Dict[str, Any]]
        Free-form user data.
    """
    billing_address: Optional[Dict[str, Any]] = Field(default=None, alias='billing_address')
    buyer: Optional[Dict[str, Any]] = Field(default=None, alias='buyer')
    cart_id: Optional[str] = Field(default=None, alias='cart_id')
    channel_id: Optional[str] = Field(default=None, alias='channel_id')
    contact_id: Optional[str] = Field(default=None, alias='contact_id')
    currency: Optional[str] = Field(default=None, alias='currency')
    customer_order_number: Optional[str] = Field(default=None, alias='customer_order_number')
    grand_total: Optional[float] = Field(default=None, alias='grand_total')
    items: List[OrderItemCreateRequest] = Field(..., alias='items')
    market_id: Optional[str] = Field(default=None, alias='market_id')
    metadata: Optional[Dict[str, Any]] = Field(default=None, alias='metadata')
    organization_id: Optional[str] = Field(default=None, alias='organization_id')
    payment: Optional[Dict[str, Any]] = Field(default=None, alias='payment')
    shipping: Optional[Dict[str, Any]] = Field(default=None, alias='shipping')
    shipping_address: Optional[Dict[str, Any]] = Field(default=None, alias='shipping_address')
    shipping_total: Optional[float] = Field(default=None, alias='shipping_total')
    user_data: Optional[Dict[str, Any]] = Field(default=None, alias='user_data')
