from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.price_ending_rule import PriceEndingRule

class PriceEntriesLadderRequest(AppwriteModel):
    """
    The quantity ladder (Staffelpreise) for ONE item, generated instead of typed: a price at the first tier and a discount compounded per tier. Identify the item with &#039;product_id&#039; or &#039;sku&#039;.

    Attributes
    ----------
    base_price : float
        Price for ONE unit at the FIRST tier, in the list’s currency and on the list’s tax basis — a decimal amount in major units (19.90), never minor units/cents.
    discount_percent : Optional[float]
        Discount applied per tier, COMPOUNDED down the ladder rather than off the base price: 5 gives 19.90 / 18.91 / 17.96. Default 0.
    product_id : Optional[str]
        The item the ladder prices.
    quantities : Optional[List[Any]]
        Tier thresholds, ascending — an array of numbers or a comma-separated string (&#039;1, 10, 50&#039;). Duplicates are collapsed and the set is sorted. Default [1, 10, 50], at most 50 tiers.
    replace : Optional[bool]
        Default true: the item&#039;s existing entries in this list are removed first, so the ladder IS the ladder. false appends.
    rounding : Optional[PriceEndingRule]
        Ending the computed prices snap to (nearest match). Omit to use the tenant&#039;s bulk_adjust_rounding setting.
    sku : Optional[str]
        The item the ladder prices (alternative to product_id).
    unit : Optional[str]
        Unit of measure carried onto every generated tier. Free text, neither validated nor converted.
    """
    base_price: float = Field(..., alias='base_price')
    discount_percent: Optional[float] = Field(default=None, alias='discount_percent')
    product_id: Optional[str] = Field(default=None, alias='product_id')
    quantities: Optional[List[Any]] = Field(default=None, alias='quantities')
    replace: Optional[bool] = Field(default=None, alias='replace')
    rounding: Optional[PriceEndingRule] = Field(default=None, alias='rounding')
    sku: Optional[str] = Field(default=None, alias='sku')
    unit: Optional[str] = Field(default=None, alias='unit')
