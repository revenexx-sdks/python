from typing import Any, Dict, List, Optional, Union, cast, Generic, TypeVar, Type
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .cart_item_snapshot import CartItemSnapshot
from ..enums.cart_item_type import CartItemType

T = TypeVar('T')

class CartItem(AppwriteModel, Generic[T]):
    """
    

    Attributes
    ----------
    cart_id : Optional[str]
        The cart this line belongs to. A line never moves between carts — a merge copies it into the target and closes the source cart.
    configuration : Optional[Dict[str, Any]]
        What was configured on this line, in the configurator&#039;s own vocabulary — this app stores it and reads nothing out of it. Its mere PRESENCE is behaviour: a line that carries a configuration never merges with another, because two differently configured units of the same article are not one line. Keys are the configurator&#039;s; the example is one shape, not the shape.
    created_at : Optional[str]
        When the line was added. A merge into an existing line keeps the original — the quantity moved, the line did not.
    currency : Optional[str]
        ISO 4217 code this line is priced in. Defaults to the cart&#039;s currency when a line is added without one.
    id : Optional[str]
        The line, as carts.items.get/update/delete address it.
    line_total : Optional[float]
        quantity × unit_price, net, always derived. A line_total in a payload is ignored: the cart may not disagree with its own arithmetic.
    metadata : Optional[Dict[str, Any]]
        Free-form data the storefront hangs on the line. Stored and returned verbatim; no key in here is read by this app.
    name : Optional[str]
        What the line reads as on the cart page. Falls back to the SKU when a caller sends none, so a line always has something to show.
    position : Optional[float]
        Sort order within the cart, ascending. Lines come back in this order unless `order` says otherwise, and a bulk replace numbers them by their place in the payload.
    product_id : Optional[str]
        The catalogue product this line came from, when it came from one. Null on a custom line, and null on a product line the storefront identified by SKU alone.
    quantity : Optional[float]
        How much of it. Fractional on purpose — 2.5 metres of cable is a line, not a rounding error — and always greater than zero: removing a line is a DELETE, not a quantity of 0.
    sku : Optional[str]
        The article number the merchant sorts by in the ERP — the value every integration joins on. Free text here: this app does not resolve it against the catalogue, so it is exactly what the storefront wrote into the line. Together with product_id and unit_price it decides whether adding the same article again lands on this line or opens a new one.
    snapshot : Optional[CartItemSnapshot[T]]
        The product as the buyer was shown it when this line was added — the cart&#039;s own copy, so it stays honest when the catalogue moves underneath it. Free-form apart from the price: conversion reads `unit_price` (or `price` as a fallback) and nothing else. A snapshot without a readable price leaves the line alone in both price modes, which is deliberate — a missing snapshot must never be read as &quot;free&quot;.
    tax_rate : Optional[float]
        VAT percent for this line, as a number (19 means 19 %). Stored with the line for the order to use — no total in this app includes tax.
    tenant_id : Optional[str]
        The tenant this row belongs to, echoed by the data plane.
    type : Optional[CartItemType]
        What kind of line this is. &#039;product&#039; is a catalogue line and the only type that ever merges with another. &#039;configuration&#039; is a configured product — it carries its configuration and always stands alone, because two differently configured units of the same article are not the same line. &#039;custom&#039; is a free line nobody has to find in a catalogue: a service, a surcharge, a hand-typed position.
    unit : Optional[str]
        The unit the quantity is counted in (&#039;pcs&#039;, &#039;m&#039;, &#039;kg&#039;, &#039;h&#039;). Display and ERP hand-over only; this app converts nothing.
    unit_price : Optional[float]
        Net price of ONE unit, in the line&#039;s currency. This is the working price — a resync, a PUT on the line or a repricing job may have moved it since the buyer saw it. The price the buyer WAS shown lives in snapshot, and carts.order decides which of the two the order is booked on.
    updated_at : Optional[str]
        When the line last changed — including a quantity another add merged into it.
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
    snapshot: Optional[CartItemSnapshot[T]] = Field(default=None, alias='snapshot')
    tax_rate: Optional[float] = Field(default=None, alias='tax_rate')
    tenant_id: Optional[str] = Field(default=None, alias='tenant_id')
    type: Optional[CartItemType] = Field(default=None, alias='type')
    unit: Optional[str] = Field(default=None, alias='unit')
    unit_price: Optional[float] = Field(default=None, alias='unit_price')
    updated_at: Optional[str] = Field(default=None, alias='updated_at')

    @classmethod
    def with_data(cls, data: Dict[str, Any], model_type: Type[T] = dict) -> 'CartItem[T]':
        """Create CartItem instance with typed data."""
        instance = cls.model_validate(data)
        if 'snapshot' in data and data['snapshot'] is not None:
            instance.snapshot = CartItemSnapshot.with_data(
                data['snapshot'], model_type
            )
        return instance
