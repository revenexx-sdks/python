from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class InventoryAdjustItem(AppwriteModel):
    """
    One item and its SIGNED correction: &#039;product_id&#039; or &#039;sku&#039;, plus a non-zero delta.

    Attributes
    ----------
    product_id : Optional[str]
        The product to move, as the products app knows it. Give this OR `sku` — an item that names neither is answered 400. Matching is exact: a stock row keyed by SKU is not found by product id.
    quantity : float
        The SIGNED correction to `on_hand`: −3 writes off three, +3 finds three. It is a delta, not the new balance. Zero is refused (400) because a correction of nothing is a mistake, not a booking — the rule is the handler&#039;s, not a database CHECK, which is why it is stated here rather than declared as a bound.
    sku : Optional[str]
        The article number to move, when the item has no product id. Give this OR `product_id`.
    """
    product_id: Optional[str] = Field(default=None, alias='product_id')
    quantity: float = Field(..., alias='quantity')
    sku: Optional[str] = Field(default=None, alias='sku')
