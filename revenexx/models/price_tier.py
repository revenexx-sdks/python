from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class PriceTier(AppwriteModel):
    """
    One rung of the winning list’s quantity ladder for this item.

    Attributes
    ----------
    quantity_min : Optional[float]
        The quantity this rung applies from. The rung with the highest `quantity_min` at or below the requested quantity is the one `unit_price` on the item was taken from.
    unit : Optional[str]
        Unit of measure the rung’s price is per. Absent when the entry names none.
    unit_price : Optional[float]
        The rung’s price for ONE unit, in the answer’s `currency` and on the item’s `tax_basis` — decimal major units, exactly as stored. Tiers are NOT tax-adjusted: only the chosen price gets `unit_price_net`/`unit_price_gross`.
    """
    quantity_min: Optional[float] = Field(default=None, alias='quantity_min')
    unit: Optional[str] = Field(default=None, alias='unit')
    unit_price: Optional[float] = Field(default=None, alias='unit_price')
