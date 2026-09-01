from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class OrderCancelPosition(AppwriteModel):
    """
    A position quantity to cancel — guarded against the open (unshipped, uncancelled) quantity.

    Attributes
    ----------
    order_item_id : str
        The order item (position) to act on. Read the ids from GET /orders/{id} (items[].id) or GET /orders/{id}/shippable (positions[].order_item_id) — an id this order does not carry is a 400.
    quantity : Optional[float]
        Defaults to the full remaining quantity of the position.
    """
    order_item_id: str = Field(..., alias='order_item_id')
    quantity: Optional[float] = Field(default=None, alias='quantity')
