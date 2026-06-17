from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class ShippingRateTierReplaceItem(AppwriteModel):
    """
    A matrix tier of the new set (from_value → price) — null falls back to 0, position derives from the array order.

    Attributes
    ----------
    from_value : Optional[float]
        Tier threshold (default 0) — the tier with the highest from_value at or below the measured value wins.
    position : Optional[float]
        Ignored — derived from the array index.
    price : Optional[float]
        Price of this tier (default 0).
    """
    from_value: Optional[float] = Field(default=None, alias='from_value')
    position: Optional[float] = Field(default=None, alias='position')
    price: Optional[float] = Field(default=None, alias='price')
