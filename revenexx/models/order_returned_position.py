from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class OrderReturnedPosition(AppwriteModel):
    """
    One position quantity registered for return.

    Attributes
    ----------
    order_item_id : Optional[str]
        The order item this quantity was booked against — an id out of the same order, never another one.
    quantity : Optional[float]
        The quantity booked on that position, in the position&#039;s own unit. Three decimal places, so 0.5 m of cable is a real booking.
    restock : Optional[bool]
        Whether this quantity is reported for restocking when the return completes. Restocking itself stays an explicit inventories.restock call by the orchestrator — this app never writes another app&#039;s stock.
    """
    order_item_id: Optional[str] = Field(default=None, alias='order_item_id')
    quantity: Optional[float] = Field(default=None, alias='quantity')
    restock: Optional[bool] = Field(default=None, alias='restock')
