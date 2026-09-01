from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class InventoryStockItem(AppwriteModel):
    """
    One item and how much of it: &#039;product_id&#039; or &#039;sku&#039;, plus a positive quantity.

    Attributes
    ----------
    product_id : Optional[str]
        The product to move, as the products app knows it. Give this OR `sku` — an item that names neither is answered 400. Matching is exact: a stock row keyed by SKU is not found by product id.
    quantity : float
        How many units this booking moves. Always POSITIVE here — the direction is the route (receive adds, reserve holds, restock returns), not the sign. Zero or a negative number is answered 400; a signed correction is what POST /inventories/adjust is for.
    sku : Optional[str]
        The article number to move, when the item has no product id. Give this OR `product_id`.
    """
    product_id: Optional[str] = Field(default=None, alias='product_id')
    quantity: float = Field(..., alias='quantity')
    sku: Optional[str] = Field(default=None, alias='sku')
