from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class InventoryAvailabilityItem(AppwriteModel):
    """
    An item to check: &#039;product_id&#039; or &#039;sku&#039;.

    Attributes
    ----------
    product_id : Optional[str]
        Typed model field.
    quantity : Optional[float]
        Requested quantity for the orderable check (default 1).
    sku : Optional[str]
        Typed model field.
    """
    product_id: Optional[str] = Field(default=None, alias='product_id')
    quantity: Optional[float] = Field(default=None, alias='quantity')
    sku: Optional[str] = Field(default=None, alias='sku')
