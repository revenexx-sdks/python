from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .price_entry import PriceEntry
from ..enums.price_ending_rule import PriceEndingRule
from ..enums.price_rounding_mode import PriceRoundingMode

class PriceEntriesLadderResponse(AppwriteModel):
    """
    The generated ladder as stored, plus the rounding policy that shaped it.

    Attributes
    ----------
    entries : Optional[List[PriceEntry]]
        The generated rungs, one per requested quantity, ascending — this IS the item&#039;s ladder in this list.
    precision : Optional[float]
        Decimals each tier was rounded to before snapping — the tenant&#039;s price_precision.
    replaced : Optional[bool]
        true when the item&#039;s existing entries in this list were removed first (the default), so the answer is the whole ladder rather than an addition to one.
    rounding : Optional[PriceEndingRule]
        The price ending each tier was snapped to — the request&#039;s, or the tenant&#039;s bulk_adjust_rounding.
    rounding_mode : Optional[PriceRoundingMode]
        How they landed on the last decimal — the tenant&#039;s rounding_mode.
    """
    entries: Optional[List[PriceEntry]] = Field(default=None, alias='entries')
    precision: Optional[float] = Field(default=None, alias='precision')
    replaced: Optional[bool] = Field(default=None, alias='replaced')
    rounding: Optional[PriceEndingRule] = Field(default=None, alias='rounding')
    rounding_mode: Optional[PriceRoundingMode] = Field(default=None, alias='rounding_mode')
