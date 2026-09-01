from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class PriceResolveItem(AppwriteModel):
    """
    Identify by &#039;product_id&#039; or &#039;sku&#039; — an item without identity resolves to on_request with a per-item error rather than failing the call.

    Attributes
    ----------
    product_id : Optional[str]
        Product to price.
    quantity : Optional[float]
        Requested quantity, counted in the entry’s `unit`. It picks the tier (the highest `quantity_min` at or below it) and multiplies into `line_total`. Default 1; a non-positive value falls back to 1.
    sku : Optional[str]
        SKU to price (alternative to product_id). Matched exactly against the entries’ own `sku`.
    """
    product_id: Optional[str] = Field(default=None, alias='product_id')
    quantity: Optional[float] = Field(default=None, alias='quantity')
    sku: Optional[str] = Field(default=None, alias='sku')
