from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .inventory_availability_item import InventoryAvailabilityItem

class InventoryAvailabilityRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    items : Optional[List[InventoryAvailabilityItem]]
        The items to check, at most 200 in one call. A cart, a category page, a feed row — one call answers them all, which is why this route is the batch one.
    location_code : Optional[str]
        Restrict the check to ONE location, by its code — the stock a click-and-collect store can promise today. Omitted, every ENABLED location is summed; a disabled one is never counted either way.
    product_id : Optional[str]
        Inline single-item form: the product to move, instead of a one-entry `items` array. The two forms are equivalent — nothing downstream knows which arrived.
    quantity : Optional[float]
        Inline single-item form: how many are wanted (default 1). It decides `orderable` and nothing else.
    sku : Optional[str]
        Inline single-item form: the article number to move (instead of `product_id`).
    """
    items: Optional[List[InventoryAvailabilityItem]] = Field(default=None, alias='items')
    location_code: Optional[str] = Field(default=None, alias='location_code')
    product_id: Optional[str] = Field(default=None, alias='product_id')
    quantity: Optional[float] = Field(default=None, alias='quantity')
    sku: Optional[str] = Field(default=None, alias='sku')
