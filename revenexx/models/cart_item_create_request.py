from typing import Any, Dict, List, Optional, Union, cast, Generic, TypeVar, Type
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .cart_item_snapshot import CartItemSnapshot
from ..enums.cart_item_type import CartItemType

T = TypeVar('T')

class CartItemCreateRequest(AppwriteModel, Generic[T]):
    """
    An item needs an identity: &#039;name&#039; or &#039;sku&#039;.

    Attributes
    ----------
    configuration : Optional[Dict[str, Any]]
        What was configured on this line, in the configurator&#039;s own vocabulary — this app stores it and reads nothing out of it. Its mere PRESENCE is behaviour: a line that carries a configuration never merges with another, because two differently configured units of the same article are not one line. Keys are the configurator&#039;s; the example is one shape, not the shape.
    currency : Optional[str]
        ISO 4217 code. Defaults to the cart&#039;s currency.
    metadata : Optional[Dict[str, Any]]
        Free-form data the storefront hangs on the line. Stored and returned verbatim; no key in here is read by this app.
    name : Optional[str]
        What the line reads as on the cart page. Falls back to &#039;sku&#039; when omitted, so a line always has something to show.
    position : Optional[float]
        Sort order within the cart, ascending. Default 0 when adding a line; in a bulk replace the payload order fills it in.
    product_id : Optional[str]
        The catalogue product, when the line comes from one. Part of the merge identity: same product, same price, one line.
    quantity : Optional[float]
        How much of it — default 1. Fractional is legal (2.5 m of cable); zero and negative are not. On a plain product line that merges into an existing one, this is ADDED to what is already there, and max_quantity_per_line is checked on the result.
    sku : Optional[str]
        The article number, exactly as the merchant knows it. Free text — this app does not resolve it against the catalogue — and part of the merge identity together with product_id and unit_price. The example only shows the shape of a real article number; nothing here enforces one.
    snapshot : Optional[CartItemSnapshot[T]]
        The product as the buyer was shown it when this line was added — the cart&#039;s own copy, so it stays honest when the catalogue moves underneath it. Free-form apart from the price: conversion reads `unit_price` (or `price` as a fallback) and nothing else. A snapshot without a readable price leaves the line alone in both price modes, which is deliberate — a missing snapshot must never be read as &quot;free&quot;.
    tax_rate : Optional[float]
        VAT percent for this line, as a number (19 means 19 %). Stored for the order to use — no total in this app includes tax.
    type : Optional[CartItemType]
        Line type (default &#039;product&#039;). Plain product lines merge by product+price; configurations always stand alone.
    unit : Optional[str]
        The unit the quantity is counted in. Display and ERP hand-over only — this app converts nothing.
    unit_price : Optional[float]
        Net price of one unit — line_total is always derived from it, never sent. Part of the merge identity: the same article at a different price opens a new line rather than averaging into the old one.
    """
    configuration: Optional[Dict[str, Any]] = Field(default=None, alias='configuration')
    currency: Optional[str] = Field(default=None, alias='currency')
    metadata: Optional[Dict[str, Any]] = Field(default=None, alias='metadata')
    name: Optional[str] = Field(default=None, alias='name')
    position: Optional[float] = Field(default=None, alias='position')
    product_id: Optional[str] = Field(default=None, alias='product_id')
    quantity: Optional[float] = Field(default=None, alias='quantity')
    sku: Optional[str] = Field(default=None, alias='sku')
    snapshot: Optional[CartItemSnapshot[T]] = Field(default=None, alias='snapshot')
    tax_rate: Optional[float] = Field(default=None, alias='tax_rate')
    type: Optional[CartItemType] = Field(default=None, alias='type')
    unit: Optional[str] = Field(default=None, alias='unit')
    unit_price: Optional[float] = Field(default=None, alias='unit_price')

    @classmethod
    def with_data(cls, data: Dict[str, Any], model_type: Type[T] = dict) -> 'CartItemCreateRequest[T]':
        """Create CartItemCreateRequest instance with typed data."""
        instance = cls.model_validate(data)
        if 'snapshot' in data and data['snapshot'] is not None:
            instance.snapshot = CartItemSnapshot.with_data(
                data['snapshot'], model_type
            )
        return instance
