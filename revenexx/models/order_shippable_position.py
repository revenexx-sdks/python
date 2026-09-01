from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class OrderShippablePosition(AppwriteModel):
    """
    One order position with the quantity that may still be shipped, and the three numbers that quantity is made of. Every position of the order is here, including the ones with nothing left open — a dialog needs to show a fully shipped line as fully shipped, not omit it.

    Attributes
    ----------
    name : Optional[str]
        The article name as it stood at place-time, frozen. Falls back to the sku when the caller sent none — a position always reads as something.
    order_item_id : Optional[str]
        The position, by the id a positions[] payload names it with. This is what POST /orders/{id}/ship expects — copy it, do not construct it.
    position : Optional[float]
        The line number a human reads, and what the order is sorted by. Numbered in steps of the range&#039;s position_step (10, 20, 30) unless the caller set it explicitly — the gap is what lets a line be inserted later without renumbering.
    product_id : Optional[str]
        The catalog product this line was taken from (the products app). Null on a custom line, and it stays a reference — the position keeps working after the product is retired.
    quantity : Optional[float]
        How much was ORDERED on this position. Unchanged by anything that happens afterwards.
    quantity_cancelled : Optional[float]
        How much was cancelled and will never go out.
    quantity_open : Optional[float]
        quantity − shipped − cancelled: the budget POST /orders/{id}/ship guards this position against, and the largest quantity it will accept. Zero means the line is done.
    quantity_shipped : Optional[float]
        How much has already gone out.
    sku : Optional[str]
        The article number as it stood at place-time, frozen with the rest of the line. The value an ERP and a warehouse both join on, and the one field a picker reads. Null only on a line that never had one.
    unit : Optional[str]
        The unit the quantity is counted in — piece, metre, kilogram, package. Free text as the catalog carries it; this app does no conversion.
    """
    name: Optional[str] = Field(default=None, alias='name')
    order_item_id: Optional[str] = Field(default=None, alias='order_item_id')
    position: Optional[float] = Field(default=None, alias='position')
    product_id: Optional[str] = Field(default=None, alias='product_id')
    quantity: Optional[float] = Field(default=None, alias='quantity')
    quantity_cancelled: Optional[float] = Field(default=None, alias='quantity_cancelled')
    quantity_open: Optional[float] = Field(default=None, alias='quantity_open')
    quantity_shipped: Optional[float] = Field(default=None, alias='quantity_shipped')
    sku: Optional[str] = Field(default=None, alias='sku')
    unit: Optional[str] = Field(default=None, alias='unit')
