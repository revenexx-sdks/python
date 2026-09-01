from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class InventoryCommitRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    order_ref : str
        The order this hold belongs to. The caller supplies it — this app mints nothing — and it is the handle POST /inventories/release and POST /inventories/commit act on, so it has to be the same string the order carries elsewhere. At least one character (CHECK `length(order_ref) &gt; 0`). Not unique: an order holds one reservation per item, and they are released or committed together. Every ACTIVE hold under this reference ships: `on_hand` and `reserved` both fall and a `shipment` booking is written for each. Unlike release, committing an order that has nothing active is a 422 — it means the hold was already released or already shipped, and shipping twice is worth saying out loud.
    """
    order_ref: str = Field(..., alias='order_ref')
