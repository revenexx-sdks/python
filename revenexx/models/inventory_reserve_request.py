from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .inventory_stock_item import InventoryStockItem
from .inventory_ship_to import InventoryShipTo

class InventoryReserveRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    expires_at : Optional[str]
        When this hold lapses. The sweeper — POST /inventories/reservations/sweep, and the &#039;expire-reservations&#039; schedule that runs it every 15 minutes — releases everything past this moment exactly as a cancellation would, so an abandoned checkout stops holding stock on its own. Null means the row named no deadline: it is swept on its AGE instead once `reservation_ttl_minutes` is above 0, which is what makes turning that setting on retroactive. Omit it to let the `reservation_ttl_minutes` setting stamp one (0 — its default — means no deadline at all); send one to hold this order for a window of its own, e.g. a quote that stands until Friday.
    items : Optional[List[InventoryStockItem]]
        The items to hold, at most 200 in one call — a whole cart in one request. The call is planned before anything is written, so either every item is placed or nothing is.
    location_code : Optional[str]
        Where a BACKORDERED item is booked when no location holds a stock row for it at all — the last fallback, not the allocator: which location serves an item that IS in stock comes from `allocation_strategy`. Omitted, the `default_location_code` setting decides.
    order_ref : str
        The order this hold belongs to. The caller supplies it — this app mints nothing — and it is the handle POST /inventories/release and POST /inventories/commit act on, so it has to be the same string the order carries elsewhere. At least one character (CHECK `length(order_ref) &gt; 0`). Not unique: an order holds one reservation per item, and they are released or committed together. Reserving twice under the same reference ADDS holds rather than replacing them — release first if you mean to replace.
    product_id : Optional[str]
        Inline single-item form: the product to move, instead of a one-entry `items` array. The two forms are equivalent — nothing downstream knows which arrived.
    quantity : Optional[float]
        Inline single-item form: how many to hold. Positive — the hold is expressed as a positive reservation, while the ledger booking it writes carries the negative.
    ship_to : Optional[InventoryShipTo]
        Where the order is going. Read ONLY when the tenant&#039;s `allocation_strategy` is &#039;nearest&#039; — under &#039;priority&#039; or &#039;single_location&#039; it is accepted and ignored, so sending it is never wrong, it is just not always heard.
    sku : Optional[str]
        Inline single-item form: the article number to move (instead of `product_id`).
    """
    expires_at: Optional[str] = Field(default=None, alias='expires_at')
    items: Optional[List[InventoryStockItem]] = Field(default=None, alias='items')
    location_code: Optional[str] = Field(default=None, alias='location_code')
    order_ref: str = Field(..., alias='order_ref')
    product_id: Optional[str] = Field(default=None, alias='product_id')
    quantity: Optional[float] = Field(default=None, alias='quantity')
    ship_to: Optional[InventoryShipTo] = Field(default=None, alias='ship_to')
    sku: Optional[str] = Field(default=None, alias='sku')
