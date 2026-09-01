from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .inventory_stock_item import InventoryStockItem

class InventoryReceiveRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    items : Optional[List[InventoryStockItem]]
        The goods that arrived, at most 200 in one call — a delivery, a production batch, an opening balance.
    location_code : Optional[str]
        Which location took the delivery. Omitted, the `default_location_code` setting decides; a code no location carries is answered 400 rather than booked somewhere else.
    product_id : Optional[str]
        Inline single-item form: the product to move, instead of a one-entry `items` array. The two forms are equivalent — nothing downstream knows which arrived.
    quantity : Optional[float]
        Inline single-item form: how many arrived. Positive.
    reason : Optional[str]
        What the ledger should record about this receipt — a delivery note number, a production order. Owed only when `movement_reason_required` is &#039;all&#039;; the contract does not require it, because whether it is owed is the tenant&#039;s setting and not this route&#039;s rule.
    sku : Optional[str]
        Inline single-item form: the article number to move (instead of `product_id`).
    """
    items: Optional[List[InventoryStockItem]] = Field(default=None, alias='items')
    location_code: Optional[str] = Field(default=None, alias='location_code')
    product_id: Optional[str] = Field(default=None, alias='product_id')
    quantity: Optional[float] = Field(default=None, alias='quantity')
    reason: Optional[str] = Field(default=None, alias='reason')
    sku: Optional[str] = Field(default=None, alias='sku')
