from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .inventory_stock_item import InventoryStockItem

class InventoryReceiveRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    items : List[InventoryStockItem]
        The inbound items (at most 200).
    location_code : Optional[str]
        Receiving location (default &#039;main&#039;).
    reason : Optional[str]
        Ledger note (e.g. delivery note number).
    """
    items: List[InventoryStockItem] = Field(..., alias='items')
    location_code: Optional[str] = Field(default=None, alias='location_code')
    reason: Optional[str] = Field(default=None, alias='reason')
