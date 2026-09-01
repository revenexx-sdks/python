from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class PriceAdjustPreviewRow(AppwriteModel):
    """
    One entry, before and after — the row a confirmation dialog shows.

    Attributes
    ----------
    id : Optional[str]
        The price entry this row is about.
    new_unit_price : Optional[float]
        After rounding and ending snapping, in the same currency and on the same basis. Never negative: below the lowest candidate ending it clamps to it.
    product_id : Optional[str]
        The product it prices — null when the entry is identified by SKU.
    quantity_min : Optional[float]
        Which rung of the ladder this is.
    sku : Optional[str]
        The SKU it prices — null when the entry is identified by product id.
    unit_price : Optional[float]
        Before the change, in the list’s currency and on its tax basis.
    """
    id: Optional[str] = Field(default=None, alias='id')
    new_unit_price: Optional[float] = Field(default=None, alias='new_unit_price')
    product_id: Optional[str] = Field(default=None, alias='product_id')
    quantity_min: Optional[float] = Field(default=None, alias='quantity_min')
    sku: Optional[str] = Field(default=None, alias='sku')
    unit_price: Optional[float] = Field(default=None, alias='unit_price')
