from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class InventoryStockItem(AppwriteModel):
    """
    An item and its quantity: &#039;product_id&#039; or &#039;sku&#039;.

    Attributes
    ----------
    product_id : Optional[str]
        Typed model field.
    quantity : float
        Typed model field.
    sku : Optional[str]
        Typed model field.
    """
    product_id: Optional[str] = Field(default=None, alias='product_id')
    quantity: float = Field(..., alias='quantity')
    sku: Optional[str] = Field(default=None, alias='sku')
