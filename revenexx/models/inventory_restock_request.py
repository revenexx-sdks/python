from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .inventory_stock_item import InventoryStockItem

class InventoryRestockRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    items : Optional[List[InventoryStockItem]]
        The goods that came back, at most 200 in one call. Whether they rejoin sellable stock is `restock`, not this list.
    location_code : Optional[str]
        Where the goods came back to — a returns warehouse is a location like any other. Omitted, the `default_location_code` setting decides.
    order_ref : Optional[str]
        The order the goods came back from. It is written onto the ledger booking, so the return shows up in that order&#039;s stock history next to its reserve and shipment — no reservation is touched by it.
    product_id : Optional[str]
        Inline single-item form: the product to move, instead of a one-entry `items` array. The two forms are equivalent — nothing downstream knows which arrived.
    quantity : Optional[float]
        Inline single-item form: how many came back. Positive.
    reason : Optional[str]
        Why the goods came back — &#039;wrong size&#039;, &#039;damaged on arrival&#039;. Owed only when `movement_reason_required` is &#039;all&#039;.
    restock : Optional[bool]
        Do these goods rejoin SELLABLE stock? A merchant decision, not a fact: apparel usually restocks, hygiene articles never do, many merchants inspect first. Omit it to follow the `restock_on_return_default` setting. `false` answers `restocked: false`, moves nothing and books NOTHING — there is no movement to write, because no stock moved, and that is the branch that makes this route a 200 while its sibling `receive` is a 201.
    sku : Optional[str]
        Inline single-item form: the article number to move (instead of `product_id`).
    """
    items: Optional[List[InventoryStockItem]] = Field(default=None, alias='items')
    location_code: Optional[str] = Field(default=None, alias='location_code')
    order_ref: Optional[str] = Field(default=None, alias='order_ref')
    product_id: Optional[str] = Field(default=None, alias='product_id')
    quantity: Optional[float] = Field(default=None, alias='quantity')
    reason: Optional[str] = Field(default=None, alias='reason')
    restock: Optional[bool] = Field(default=None, alias='restock')
    sku: Optional[str] = Field(default=None, alias='sku')
