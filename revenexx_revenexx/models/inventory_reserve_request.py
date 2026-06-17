from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .inventory_stock_item import InventoryStockItem

class InventoryReserveRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    expires_at : Optional[str]
        Optional reservation expiry.
    items : List[InventoryStockItem]
        The items to reserve — all-or-nothing (at most 200).
    order_ref : str
        The order this reservation belongs to.
    """
    expires_at: Optional[str] = Field(default=None, alias='expires_at')
    items: List[InventoryStockItem] = Field(..., alias='items')
    order_ref: str = Field(..., alias='order_ref')
