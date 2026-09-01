from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .order_shippable_order import OrderShippableOrder
from .order_shippable_position import OrderShippablePosition

class OrderShippable(AppwriteModel):
    """
    What a shipment of this order may still contain, and whether one would be accepted at all — answered by the same code POST /orders/{id}/ship runs, so the two cannot drift.

    Attributes
    ----------
    blocked_reason : Optional[str]
        Why not, in the very words POST /orders/{id}/ship would refuse with — including the hold reason where there is one. Null when `shippable` is true.
    open_positions : Optional[float]
        How many positions still have an open quantity — the number of lines a shipment dialog would offer.
    open_quantity : Optional[float]
        The summed open quantity over those positions. Mixes units where the order does, so it is a headline figure, not a total to act on.
    order : Optional[OrderShippableOrder]
        Just enough of the order to render the answer — the full row is GET /orders/{id}.
    positions : Optional[List[OrderShippablePosition]]
        Every position of the order, in position order, each with its open quantity.
    shippable : Optional[bool]
        Whether a shipment would be accepted RIGHT NOW — the one question a &quot;create shipment&quot; button should be enabled on. False when the order is held, cancelled, completed, or has nothing open.
    """
    blocked_reason: Optional[str] = Field(default=None, alias='blocked_reason')
    open_positions: Optional[float] = Field(default=None, alias='open_positions')
    open_quantity: Optional[float] = Field(default=None, alias='open_quantity')
    order: Optional[OrderShippableOrder] = Field(default=None, alias='order')
    positions: Optional[List[OrderShippablePosition]] = Field(default=None, alias='positions')
    shippable: Optional[bool] = Field(default=None, alias='shippable')
