from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class OrderReturnPosition(AppwriteModel):
    """
    A position quantity to return — guarded against the shipped (not yet returned) quantity.

    Attributes
    ----------
    order_item_id : str
        The order item (position) to act on. Read the ids from GET /orders/{id} (items[].id) or GET /orders/{id}/shippable (positions[].order_item_id) — an id this order does not carry is a 400.
    quantity : Optional[float]
        Defaults to the full remaining quantity of the position.
    restock : Optional[bool]
        Report this position for restocking when the return completes (the explicit inventories.restock call stays with the orchestrator).
    """
    order_item_id: str = Field(..., alias='order_item_id')
    quantity: Optional[float] = Field(default=None, alias='quantity')
    restock: Optional[bool] = Field(default=None, alias='restock')
