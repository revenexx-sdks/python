from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class InventoryAvailabilityItem(AppwriteModel):
    """
    One item to check: &#039;product_id&#039; or &#039;sku&#039;. Checking is free of consequence — it books nothing and holds nothing.

    Attributes
    ----------
    product_id : Optional[str]
        The product to move, as the products app knows it. Give this OR `sku` — an item that names neither is answered 400. Matching is exact: a stock row keyed by SKU is not found by product id.
    quantity : Optional[float]
        How many are wanted. It only decides `orderable`; the on_hand / reserved / available figures come back whatever it is. Omit it (or send null) to ask &quot;is this sellable at all?&quot;, which is a check against 1.
    sku : Optional[str]
        The article number to move, when the item has no product id. Give this OR `product_id`.
    """
    product_id: Optional[str] = Field(default=None, alias='product_id')
    quantity: Optional[float] = Field(default=None, alias='quantity')
    sku: Optional[str] = Field(default=None, alias='sku')
