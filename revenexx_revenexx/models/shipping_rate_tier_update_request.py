from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class ShippingRateTierUpdateRequest(AppwriteModel):
    """
    Partial update — omitted fields keep their current value.

    Attributes
    ----------
    from_value : Optional[float]
        Tier threshold (default 0) — the tier with the highest from_value at or below the measured value wins.
    position : Optional[float]
        Sort order (default 0; bulk replace derives it from the array index).
    price : Optional[float]
        Price of this tier (default 0).
    """
    from_value: Optional[float] = Field(default=None, alias='from_value')
    position: Optional[float] = Field(default=None, alias='position')
    price: Optional[float] = Field(default=None, alias='price')
