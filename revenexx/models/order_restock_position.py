from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class OrderRestockPosition(AppwriteModel):
    """
    One quantity to put back into stock, named the way the inventories app wants it: by product, by sku, and how much.

    Attributes
    ----------
    product_id : Optional[str]
        The catalog product to restock. Null on a custom line, which is why `sku` is carried alongside it.
    quantity : Optional[float]
        How much came back on this position, in the position&#039;s own unit.
    sku : Optional[str]
        The article number to restock — the key a warehouse actually books against.
    """
    product_id: Optional[str] = Field(default=None, alias='product_id')
    quantity: Optional[float] = Field(default=None, alias='quantity')
    sku: Optional[str] = Field(default=None, alias='sku')
