from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .inventory_stock_item import InventoryStockItem

class InventoryRestockRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    items : List[InventoryStockItem]
        The returned items (at most 200).
    location_code : Optional[str]
        Restocking location (default &#039;main&#039;).
    order_ref : Optional[str]
        Originating order (ledger reference).
    reason : Optional[str]
        Ledger note (e.g. return reason).
    """
    items: List[InventoryStockItem] = Field(..., alias='items')
    location_code: Optional[str] = Field(default=None, alias='location_code')
    order_ref: Optional[str] = Field(default=None, alias='order_ref')
    reason: Optional[str] = Field(default=None, alias='reason')
